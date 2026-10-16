#!/usr/bin/env python3
"""Benchmark TTS castellano real con sherpa-onnx. No pertenece al runtime Godot.

Modelo oficial: vits-piper-es_ES-sharvard-medium (2 voces, 22050 Hz).
La salida es una locución TÉCNICA de prueba, nunca un NPC del canon.
No descarga archivos ni altera WorldState.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
import wave

MODEL_ID = "vits-piper-es_ES-sharvard-medium"
MODEL_STEM = "es_ES-sharvard-medium"
TEXT = "Esta es una prueba técnica de síntesis de voz en castellano para Nimroel."


def verify_model(root: Path):
    required = {
        "onnx": root / (MODEL_STEM + ".onnx"),
        "tokens": root / "tokens.txt",
        "espeak": root / "espeak-ng-data",
    }
    missing = [name for name, path in required.items() if
               (not path.is_dir() if name == "espeak" else not path.is_file())]
    if missing:
        raise FileNotFoundError("Modelo incompleto: " + ", ".join(missing))
    return required


def validate_speaker(sid: int):
    if sid not in (0, 1):
        raise ValueError("Este modelo admite solo voces 0 y 1")
    return sid


def run(model_dir: Path, output_dir: Path, sid: int):
    validate_speaker(sid)
    files = verify_model(model_dir)
    import numpy as np
    import sherpa_onnx

    config = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                model=str(files["onnx"]),
                data_dir=str(files["espeak"]),
                tokens=str(files["tokens"]),
            ),
            num_threads=1,
        ),
    )
    if not config.validate():
        raise RuntimeError("Configuración sherpa-onnx no válida")
    tts = sherpa_onnx.OfflineTts(config)
    start = time.perf_counter()
    audio = tts.generate(text=TEXT, sid=sid, speed=1.0)
    elapsed = time.perf_counter() - start
    rate = int(audio.sample_rate)
    samples = np.asarray(audio.samples)
    if rate <= 0 or samples.size < 1000 or not np.all(np.isfinite(samples)):
        raise RuntimeError("Audio de prueba inválido")
    pcm = (np.clip(samples, -1.0, 1.0) * 32767).astype("<i2").tobytes()
    output_dir.mkdir(parents=True, exist_ok=True)
    wav_file = output_dir / f"nim03_sharvard_speaker_{sid}.wav"
    with wave.open(str(wav_file), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(rate)
        output.writeframes(pcm)
    duration = float(samples.size) / rate
    metrics = {
        "test_kind": "sherpa_onnx_offline_tts_real",
        "locale": "es-ES", "model": MODEL_ID, "speaker_id": sid,
        "host_platform": platform.platform(),
        "python": platform.python_version(),
        "sherpa_onnx": getattr(sherpa_onnx, "__version__", "1.13.8"),
        "sample_rate": rate, "samples": int(samples.size),
        "duration_seconds": round(duration, 4),
        "inference_seconds": round(elapsed, 4),
        "realtime_factor": round(elapsed / duration, 4),
        "wav_sha256": hashlib.sha256(wav_file.read_bytes()).hexdigest(),
        "device_physically_tested": False,
        "godot_voice_port_connected": False,
        "is_npc_voice": False,
    }
    result_file = output_dir / f"nim03_tts_metrics_speaker_{sid}.json"
    result_file.write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    return metrics


def main():
    parser = argparse.ArgumentParser(description="Prueba reproducible TTS castellano de sherpa-onnx")
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--speaker", type=int, default=0)
    args = parser.parse_args()
    try:
        run(args.model_dir, args.output_dir, args.speaker)
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print("NIM-03 TTS sin validar: " + str(exc), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
