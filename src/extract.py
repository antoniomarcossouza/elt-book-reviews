# %%
from pathlib import Path

from utils import download_file, json_to_parquet

PROJECT_DIR = Path.cwd()
DATA_DIR = Path(PROJECT_DIR / "data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


# %%
files = [
    "goodreads_books.json.gz",
    "goodreads_book_authors.json.gz",
    "goodreads_reviews_dedup.json.gz",
]

for file in files:
    json_path = DATA_DIR / file
    parquet_path = DATA_DIR / Path(json_path.stem).with_suffix(".parquet")

    download_file(
        url=f"https://datarepo.eng.ucsd.edu/mcauley_group/gdrive/goodreads/{file}",
        output_file=json_path,
    )
    json_to_parquet(
        input_file=json_path,
        output_file=parquet_path,
    )
