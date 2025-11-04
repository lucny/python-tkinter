import csv
from pathlib import Path


def load_data(csv_path="world_happiness_2024.csv"):
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Soubor {csv_path} nebyl nalezen.")

    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data
