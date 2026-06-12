#app_dir = Path(__file__).parent
#df = pd.read_csv(app_dir / "penguins.csv")
from pathlib import Path
import pandas as pd

ruta = Path(__file__).parent /"../data/processed"

ultimas_valuaciones = pd.read_parquet(ruta / "ultimas_valuaciones.parquet")
historico_valuaciones = pd.read_parquet(ruta / "historico_valuaciones.parquet")
rendimiento_equipos = pd.read_parquet(ruta / "rendimiento_equipos.parquet")

lista_jugadores = sorted(historico_valuaciones["name"].dropna().unique())
lista_equipos = sorted(rendimiento_equipos["Equipo"].dropna().unique())

jugador1_mas_valioso = ultimas_valuaciones.sort_values("market_value_millon",ascending=False).iloc[0]["name"]
jugador2_mas_valioso = ultimas_valuaciones.sort_values("market_value_millon",ascending=False).iloc[1]["name"]