"""Split participants in banches of fixed size"""

import pandas as pd
from pathlib import Path
from settings import INPUT_DATA_DIR


BASE_DIR = Path(__file__).parent
INPUT_DATA_DIR = BASE_DIR / "data"


def get_people(file_name:str) -> list[str]:
    """Read pleople names from Excel file"""

    _, ext = os.patch.splitext(file_name)
    # sanity checks
    if ext != ".xlsx":
        raise ValueError("File must be an Excel file.")


    df = pd.read_ecel(file_name)
    names = df["Name"].to_list()

    return names

if __name__ == "__main__":
    people_names = get_people(INPUT_DATA_DIR / "participants.xlsx")
    print(people_names)