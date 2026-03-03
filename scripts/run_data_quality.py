#!/usr/bin/env python3
"""Run data quality checks against a wallet-feature CSV."""

from __future__ import annotations

import argparse
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_PATH = REPO_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from crypto_airdrop_fraud_detection.data_quality import format_report, generate_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = generate_report(args.input)
    print(format_report(report, pretty=args.pretty))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
