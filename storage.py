import json
from pathlib import Path


def check_records(records):
    if not isinstance(records, list):
        raise ValueError("Expenses must be a list.")

    for expense in records:
        if not isinstance(expense, dict):
            raise ValueError("Each expense must be a dictionary.")


def load_records(path):
    path = Path(path)

    try:
        with path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        return []

    check_records(records)
    return records


def save_records(path, records):
    check_records(records)

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    temp_path = path.with_name(path.name + ".tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)

    temp_path.replace(path)