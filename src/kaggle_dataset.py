# %%
from pathlib import Path

import kaggle

from logger import create_logger

LOGGER = create_logger()


# %%
def kaggle_download(dataset: str, output_dir: Path) -> None:
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(
        dataset=dataset,
        path=output_dir,
        unzip=True,
    )
    LOGGER.info(f"Dataset {dataset} baixado.")
