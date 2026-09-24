from pathlib import Path
from urllib.request import urlopen

import pandas as pd


DEFAULT_URL = (
    "https://datos.gob.do/dataset/"
    "estadisticas-de-pruebas-nacionales-2016-2024"
)


def download_csv(url: str, output_path: str) -> Path:
    """Descarga un archivo CSV desde una URL y lo guarda localmente."""
    if not url or not url.startswith(("http://", "https://")):
        raise ValueError("La URL debe comenzar con http:// o https://")

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    with urlopen(url) as response:
        destination.write_bytes(response.read())

    return destination


def load_student_performance(
    path: str,
    sep: str = ";",
    encoding: str = "latin1",
) -> pd.DataFrame:
    """Carga el archivo de Pruebas Nacionales desde una ruta local."""
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"No existe el archivo: {file_path}")

    df = pd.read_csv(
        file_path,
        sep=sep,
        encoding=encoding,
    )

    if df.empty:
        raise ValueError("El archivo descargado está vacío.")

    return df


def download_student_performance(
    url: str,
    output_path: str = "data/raw/pruebas_nacionales_2016_2024.csv",
) -> Path:
    """Descarga reproduciblemente el dataset de Pruebas Nacionales."""
    return download_csv(url, output_path)