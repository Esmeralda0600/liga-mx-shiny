from shinywidgets import render_widget
import plotly.express as px
from ligamx_shiny import shared

def mercado_server(input,output,session):
    @render_widget
    def grafico_top():
        top_jugadores = shared.ultimas_valuaciones.sort_values("market_value_millon", ascending=False).head(15)
        fig = px.bar(
            top_jugadores,
            x="market_value_millon",
            y="name",
            orientation="h",
            text_auto=".2f",
            labels={
                "market_value_millon": "Valor de Mercado (Millones €)",
                "name": "Jugador"
            },
            title="Top 15 jugadores más valiosos",
            color="market_value_millon",
            color_continuous_scale="Viridis",
            template="plotly_dark"
        )
        fig.update_layout(yaxis={"categoryorder":"total ascending"})
        return fig
    
    @render_widget
    def grafico_historico():
        j_a = input.jugador_a()
        j_b = input.jugador_b()
        
        filtrado = shared.historico_valuaciones[
            shared.historico_valuaciones["name"].isin([j_a, j_b])
        ].copy()
        
        fig_linea = px.line(
            filtrado,
            x="date",
            y="market_value_millon",
            color="name",
            markers=True,
            labels={
                "date": "Fecha de Valuacion",
                "market_value_millon": "Valor de Mercado (Millones €)",
                "name": "Futbolista"
            },
            title=f"{j_a} vs {j_b}",
            template="plotly_dark",
            color_discrete_sequence=["#00FFCC", "#FF3366"]
        )
        fig_linea.update_layout(hovermode="x unified")
        return fig_linea
    
def rendimiento_server(input,output,session):

    @render_widget
    def grafico_rendimiento_equipos():
        club = input.equipo_rendimiento()
        
        filtrado = shared.rendimiento_equipos[
            shared.rendimiento_equipos["Equipo"] == club
        ]
        
        fig = px.bar(
            filtrado,
            x="year",
            y="Partidos",
            color="Rendimiento",
            title=f"{club} (Temporadas 2016 - 2024)",
            labels={
                "year": "Año",
                "Partidos": "Cantidad de Partidos",
                "Rendimiento": "Resultado"
            },
            color_discrete_map={
                "Victoria": "#00FF5E",
                "Empate": "#3399FF",
                "Derrota": "#FF3333"
            },
            template="plotly_dark"
        )
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                tick0=2016,
                dtick=1
            ),
            barmode="stack"
        )
        return fig
        