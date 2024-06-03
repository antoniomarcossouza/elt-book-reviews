import os
import urllib.request
from pathlib import Path

import duckdb
from dotenv import load_dotenv
from google.cloud import bigquery, storage

from logger import create_logger

load_dotenv()

LOGGER = create_logger()
PROJECT_ID = os.environ["PROJECT_ID"]
STAGING_DATASET_ID = os.environ["STAGING_DATASET_ID"]


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
    input_file: str, output_file: str, columns: list[str] = ["*"]
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


def load_data(input_file: Path, bucket_name: str, output_file: str) -> None:
    """Função que faz upload de um arquivo para o
    Google Cloud Storage e cria uma external table no BigQuery.

    Parâmetros
    ----------
    input_file : Path
        caminho do arquivo a ser enviado.
    bucket_name : str
        nome do bucket no Google Cloud Storage.
    output_file : str
        caminho do arquivo no bucket.
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path.cwd() / "credentials.json")

    gcs_client = storage.Client()
    bucket = gcs_client.bucket(bucket_name)
    blob = bucket.blob(output_file)
    blob.upload_from_filename(input_file)
    LOGGER.info(
        f"Arquivo {input_file} enviado para o bucket {bucket_name} no caminho {output_file}."
    )

    bq_client = bigquery.Client()
    external_config = bigquery.ExternalConfig("PARQUET")
    external_config.source_uris = f"gs://{bucket_name}/{output_file}"
    table = bigquery.Table(
        bq_client.dataset(STAGING_DATASET_ID).table(output_file.replace(".parquet", ""))
    )
    table.external_data_configuration = external_config
    table = bq_client.create_table(table, exists_ok=True)
    LOGGER.info(f"Tabela {output_file} criada no BigQuery.")
