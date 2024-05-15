# %%
from pathlib import Path

import kaggle

from logger import create_logger

LOGGER = create_logger()


# %%
def kaggle_download(dataset: str, output_dir: Path) -> None:
    """Função que baixa um dataset do Kaggle.
    
    Parâmetros
    ----------
    dataset : str
        nome do dataset a ser baixado
    output_dir : Path
        diretório que o arquivo será salvo
    """
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(
        dataset=dataset,
        path=output_dir,
        unzip=True,
    )
    LOGGER.info(f"Dataset {dataset} baixado.")
