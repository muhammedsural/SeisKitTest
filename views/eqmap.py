from dash import html
import sys
import dash_mantine_components as dmc
sys.path.append('./')
from components.navbar import navbarComponent, footerComponent

header = html.Div(className="col-12 col-md-12 mt-4 text-center", children=[
                dmc.Title("This page is still under construction!", className="fs-3"),
            ])

def layout():
    return html.Div([
        navbarComponent,
        header,
        footerComponent
    ])
