import urllib.request
from pathlib import Path

import duckdb

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


def json_to_parquet(
    input_file: str,
    output_file: str,
    columns: list[str] = ["*"]
) -> None:
    """Função que converte um arquivo JSON para Parquet.

    Parâmetros
    ----------
    input_file : str
        caminho do arquivo JSON a ser convertido.
    output_file : str
        caminho do arquivo Parquet a ser criado.
    """

    duckdb.sql(
        f"COPY(SELECT {", ".join(columns)} FROM read_json_auto('{input_file}')) TO '{output_file}' (FORMAT 'parquet');"
    )
    LOGGER.info(f"Arquivo {output_file} criado.")
