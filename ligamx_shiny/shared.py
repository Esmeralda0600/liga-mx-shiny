from pathlib import Path

import pandas as pd

#app_dir = Path(__file__).parent
#df = pd.read_csv(app_dir / "penguins.csv")
ruta = Path(__file__).parent /"../data/processed"

partidos = pd.read_parquet(ruta / "partidos.parquet")
ultimas_valuaciones = pd.read_parquet(ruta / "ultimas_valuaciones.parquet")
historico_valuaciones = pd.read_parquet(ruta / "historico_valuaciones.parquet")

lista_jugadores = sorted(historico_valuaciones["name"].dropna().unique())