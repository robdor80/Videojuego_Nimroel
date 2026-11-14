#!/usr/bin/env python3
"""Construye SOLO archivo efimero TEST_ONLY, nunca un sector de Edranor."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from spatial import export_sector
from test_spatial import packet, production


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    p, registry = production(packet())
    lab = export_sector(p, registry)
    assert lab["maturity"] == "LAB_GEOMETRY_NON_CANON_NOT_RUNTIME"
    assert lab["sectorId"] == "TEST_SECTOR_ONLY"
    assert lab["authorization"]["sourceId"] == "SOURCE:sector"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(lab, sort_keys=True,
                                     ensure_ascii=False, indent=2)+"\n",
                           encoding="utf-8")
    print("E19-TEC: fixture marcado LAB, no exportacion B3")


if __name__ == "__main__":
    main()
