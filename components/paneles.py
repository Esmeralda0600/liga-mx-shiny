from shiny import ui
from shinywidgets import output_widget

from ligamx_shiny import shared
#import shared

def panel_mercado_jugadores():
    return ui.nav_panel(
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
        )
        
def panel_rendimiento_equipos():
    return ui.nav_panel(
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
        
    