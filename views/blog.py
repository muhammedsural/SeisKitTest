from dash import html
import sys
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
sys.path.append('./')
from components.navbar import navbarComponent, footerComponent

header = html.Div(className="col-12 col-md-12 mt-4 text-center", children=[
                dmc.Title("Blog Posts", className="fs-3"),
                dmc.Text("Latest insights and updates from our team")
            ])

blogPost_1 = dbc.Col([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H3("SeisScale Logic 🚀", className="card-title"),
                    html.P("Here is the verification and the scientific background of the SeisScale application.", className="card-text"),

                    dbc.Button("Read More", href="/seisscalelogic"),
                ]
            ),
            dbc.CardFooter([
                html.Small(
                    "Last updated 3 mins ago",
                    className="card-text text-muted",
                ),
            ]),
        ],
    )
], className="mt-3 custom-mx")

blogPost_2 = dbc.Col([
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H3("Earthquake Data Sources", className="card-title"),
                    html.P("Learn where you can find and download strong ground motion data.", className="card-text"),
                    dbc.Button("Read More", href="/earthquakedatasources"),
                ]
            ),
            dbc.CardFooter([
                html.Small(
                    "Last updated 3 mins ago",
                    className="card-text text-muted",
                ),
            ]),
        ],
    )
], className="mt-3 custom-mx")

def layout():
    return html.Div([
        navbarComponent,
        header,
        dbc.Container([
            dbc.Row(blogPost_1),
            dbc.Row(blogPost_2),
        ], fluid=True),
        footerComponent
    ])
