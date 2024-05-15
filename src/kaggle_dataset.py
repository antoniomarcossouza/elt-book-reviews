# %%
from pathlib import Path

import kaggle
from dotenv import load_dotenv
from logger import create_logger

load_dotenv()
kaggle.api.authenticate()
LOGGER = create_logger()


# %%
def kaggle_download(dataset: str, output_dir: Path) -> None:
    """Função que baixa um dataset do Kaggle."""

    kaggle.api.dataset_download_files(
        dataset=dataset,
        path=output_dir,
        unzip=True,
    )
    LOGGER.info(f"Dataset {dataset} baixado.")
