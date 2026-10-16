"""Comprobación de precondiciones, distinta de la inferencia sherpa real."""
import tempfile
from pathlib import Path
import unittest

from voice_tts_bench import MODEL_STEM, validate_speaker, verify_model


class VoiceModelContractTests(unittest.TestCase):
    def test_voice_identifier(self):
        self.assertEqual(validate_speaker(0), 0)
        self.assertEqual(validate_speaker(1), 1)
        for invalid in (-1, 2, 999):
            with self.assertRaises(ValueError):
                validate_speaker(invalid)

    def test_models_absent_or_partial_never_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(FileNotFoundError):
                verify_model(root)
            (root / (MODEL_STEM + ".onnx")).write_bytes(b"not-a-real-model")
            (root / "tokens.txt").write_text("fake")
            with self.assertRaises(FileNotFoundError):
                verify_model(root)
            (root / "espeak-ng-data").mkdir()
            self.assertEqual(len(verify_model(root)), 3)


if __name__ == "__main__":
    unittest.main()
