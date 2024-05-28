import os
import urllib.request
from pathlib import Path

import duckdb
from google.cloud import storage

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

def upload_to_gcs(
    input_file: Path,
    bucket_name: str,
    output_file: str
) -> None:
    """Função que faz upload de um arquivo para o Google Cloud Storage.

    Parâmetros
    ----------
    input_file : Path
        caminho do arquivo a ser enviado.
    bucket_name : str
        nome do bucket no Google Cloud Storage.
    output_file : str
        caminho do arquivo no bucket.
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(
        Path.cwd() / "credentials.json"
    )
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(output_file)

    blob.upload_from_filename(input_file)
    LOGGER.info(f"Arquivo {input_file} enviado para o bucket {bucket_name} no caminho {output_file}.")
