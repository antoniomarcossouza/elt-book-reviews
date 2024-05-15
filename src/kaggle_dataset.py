# %%
from pathlib import Path

import kaggle
from dotenv import load_dotenv

load_dotenv()
kaggle.api.authenticate()


# %%
def kaggle_download(dataset: str, output_dir: Path) -> None:
    """Função que baixa um dataset do Kaggle."""

    kaggle.api.dataset_download_files(
        dataset=dataset,
        path=output_dir,
        unzip=True,
    )
