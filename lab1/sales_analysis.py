import csv
import io
from functools import reduce
from typing import Iterable, Iterator, Optional


def tire_parse_csv(data: str) -> Iterator[dict]:
    return csv.DictReader(io.StringIO(data))


def tire_compute_revenue(rows: Iterable[dict]) -> float:
    return sum(
        map(
            lambda row: float(row["quantity"]) * float(row["price"]),
            rows
        )
    )


def tire_top_item(rows: list[dict]) -> Optional[dict]:
    return max(
        rows,
        key=lambda row: float(row["quantity"]) * float(row["price"]),
        default=None
    )


data = """item,quantity,price
айфон,15,149900
макбук,10,349000
айпад,3,97000
аирподсы,18,19900
"""


print(f"Продажи: {list(tire_parse_csv(data))}")

print(f"\nОбщая выручка: {tire_compute_revenue(tire_parse_csv(data))}")

print(f"\nСамая прибыльная позиция: {tire_top_item(tire_parse_csv(data))}")
