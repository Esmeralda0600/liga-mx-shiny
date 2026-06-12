
from shiny import App, ui
from components.paneles import panel_mercado_jugadores, panel_rendimiento_equipos
from components.server import mercado_server, rendimiento_server

app_ui = ui.page_fluid(
    ui.panel_title("Liga MX: Valuaciones y Partidos"),
    
    ui.navset_card_pill(
        panel_mercado_jugadores(),
        panel_rendimiento_equipos()
    )
)

def server(input, output, session):
    mercado_server(input,output,session)
    rendimiento_server(input,output,session)
    
app = App(app_ui, server)
