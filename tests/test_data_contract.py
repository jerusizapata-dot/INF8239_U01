import pandas as pd

TARGET = "Cantidad Promovidos"

REQUIRED = {
    "Período",
    "Convocatoria",
    "Regional",
    "Distrito",
    "Nivel/Modalidad",
    "Cantidad de estudiantes",
    "Cantidad Promovidos",
    "Cantidad Aplazados",
}


def load_data():
    return pd.read_csv(
        "data/raw/pruebas_nacionales_2016_2024.csv",
        sep=";",
        encoding="latin1"
    )


def build_target(df):
    data = df[
        (df["Período"] != 2020)
        & df["Cantidad Promovidos"].notna()
        & df["Cantidad Aplazados"].notna()
    ].drop_duplicates().copy()

    data = data[
        data["Cantidad de estudiantes"]
        == data["Cantidad Promovidos"] + data["Cantidad Aplazados"]
    ].copy()

    data = data[
        data["Cantidad Promovidos"] != data["Cantidad Aplazados"]
    ].copy()

    data["target"] = (
        data["Cantidad Promovidos"] > data["Cantidad Aplazados"]
    ).astype(int)

    return data


def test_dataset_is_not_empty():
    assert not load_data().empty


def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns)


def test_target_has_no_missing_and_two_classes():
    data = build_target(load_data())
    y = data["target"]

    assert y.notna().all()
    assert y.nunique() >= 2