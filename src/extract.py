# %%
from pathlib import Path

from utils import download_file, json_to_parquet

PROJECT_DIR = Path.cwd()
DATA_DIR = Path(PROJECT_DIR / "data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


# %%
files = {
    "goodreads_books.json.gz": [
        "book_id",
        "work_id",
        "title",
        "series",
        "title_without_series",
        "authors",
        "publisher",
        "num_pages",
        "publication_day",
        "publication_month",
        "publication_year",
        "url",
        "image_url",
    ],
    "goodreads_book_authors.json.gz": [
        "author_id",
        "name",
    ],
    "goodreads_reviews_dedup.json.gz": [
        "user_id",
        "book_id",
        "review_id",
        "rating",
        "started_at",
        "read_at",
    ],
}

for file, columns in files.items():
    json_path = DATA_DIR / file
    parquet_path = DATA_DIR / Path(json_path.stem).with_suffix(".parquet")

    download_file(
        url=f"https://datarepo.eng.ucsd.edu/mcauley_group/gdrive/goodreads/{file}",
        output_file=json_path,
    )
    json_to_parquet(
        input_file=json_path,
        output_file=parquet_path,
        columns=columns,
    )
