"""Dataset quality checks for wallet-level fraud features."""

from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataQualityReport:
    rows: int
    columns: int
    column_names: list[str]
    empty_cells: int
    duplicate_wallets: int
    target_counts: dict[str, int]

    def to_dict(self) -> dict:
        return {
            "rows": self.rows,
            "columns": self.columns,
            "column_names": self.column_names,
            "empty_cells": self.empty_cells,
            "duplicate_wallets": self.duplicate_wallets,
            "target_counts": self.target_counts,
        }


REQUIRED_COLUMNS = {
    "wallet",
    "total_txs",
    "unique_contracts",
    "total_value_eth",
    "gas_spent_eth",
    "first_tx_date",
    "last_tx_date",
    "wallet_age_days",
    "avg_tx_value",
    "tx_diversity",
    "is_suspicious",
}


def generate_report(csv_path: str | Path) -> DataQualityReport:
    csv_path = Path(csv_path)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV is empty; expected at least one data row.")

    first_row = rows[0]
    column_names = list(first_row.keys())

    missing_columns = sorted(REQUIRED_COLUMNS.difference(column_names))
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    empty_cells = 0
    wallets: list[str] = []
    target_counter: Counter[str] = Counter()

    for row in rows:
        wallets.append(row["wallet"])
        target_counter[row["is_suspicious"]] += 1
        for value in row.values():
            if value is None or value == "":
                empty_cells += 1

    duplicate_wallets = len(wallets) - len(set(wallets))

    return DataQualityReport(
        rows=len(rows),
        columns=len(column_names),
        column_names=column_names,
        empty_cells=empty_cells,
        duplicate_wallets=duplicate_wallets,
        target_counts=dict(target_counter),
    )


def format_report(report: DataQualityReport, pretty: bool = False) -> str:
    payload = report.to_dict()
    if pretty:
        return json.dumps(payload, indent=2)
    return json.dumps(payload)
