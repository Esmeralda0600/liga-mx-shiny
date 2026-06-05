#import seaborn as sns
import plotly.express as px
from shiny import App, render, ui
from shinywidgets import output_widget, render_widget

# Import data from shared.py
import shared

app_ui = ui.page_fluid(
    
    ui.panel_title("Liga MX: Valuaciones y Partidos"),
    
    ui.navset_card_pill(
        ui.nav_panel(
            "Mercado de Jugadores",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.h3("Comparador de Jugadores"),
                    
                    ui.input_select(
                        id="jugador_a",
                        label="Selecciona un jugador: ",
                        choices=shared.lista_jugadores,
                        selected="André-Pierre Gignac" if "André-Pierre Gignac" in shared.lista_jugadores else None
                    ),
                    ui.input_select(
                        id="jugador_b",
                        label="Selecciona un jugador: ",
                        choices=shared.lista_jugadores,
                        selected="Rogelio Funes Mori" if "Rogelio Funes Mori" in shared.lista_jugadores else None
                    ),
                ),
                ui.layout_columns(
                    ui.card(
                        ui.card_header("Historial Financiero Comparativo"),
                        output_widget("grafico_historico")
                    ),
                    ui.card(
                        ui.card_header("Top 15 Jugadores Más Valiosos"),
                        output_widget("grafico_top")
                    ),
                    col_widths=[12, 12]  
                )
            )
        ),
        
        ui.nav_panel(
            "Rendimiento de Equipos",
            ui.layout_sidebar(
                ui.sidebar(
                    ui.h3("Filtro de Equipos"),
                    
                    ui.input_select(
                        id="equipo_rendimiento",
                        label="Selecciona un equipo: ",
                        choices=shared.lista_equipos,
                        selected="U.N.A.M. - Pumas" if "U.N.A.M. - Pumas" in shared.lista_equipos else shared.lista_equipos[0]
                    ),
                ),
                ui.layout_columns(
                    ui.card(
                        ui.card_header("Historial de Rendimiento General por Año"),
                        output_widget("grafico_rendimiento_equipos")
                    ),
                    col_widths=[12]
                )
            )
        )
    )
)

def server(input, output, session):
    
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

app = App(app_ui, server)
