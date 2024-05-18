import urllib.request
from pathlib import Path

from logger import create_logger

LOGGER = create_logger()


def download_file(url: str, output_file: Path) -> None:
    """Função que baixa o arquivo caso ele não exista.

    Parâmetros
    ----------
    url : str
        URL do arquivo a ser baixado.
    output_file : Path
        diretório que o arquivo será salvo.
    """

    if output_file.is_file():
        LOGGER.info(f"Arquivo {output_file} já existe, pulando.")
        return

    urllib.request.urlretrieve(url, output_file)
    LOGGER.info(f"Arquivo {output_file} baixado.")
