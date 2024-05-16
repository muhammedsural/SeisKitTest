import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import html

galleryComponent = html.Div([
    html.Div(className="container mt-4", children=[
        html.Div(className="row justify-content-center", children=[
            html.Div(className="col-12 col-md-8 text-center", children=[
                dmc.Title("Application Gallery", className="fs-3"),
                dmc.Space(h=20),
                dmc.Text("Here you find the free applications developed by engineering community.", className="fs-6")
            ])
        ]),
        
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="assets/static/seisscale.png",
                            top=True,
                            style={"opacity": 0.4},
                        ),
                        dbc.CardImgOverlay(
                            dbc.CardBody(
                                [
                                    dmc.Text("🚀 SeisScale", className="card-title fs-4"),
                                    html.Div(className="mt-auto"),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Button("Go to App", color="primary", href="/seisscale"),
                                                width="auto",
                                                className="ml-auto mr-auto"
                                            )
                                        ],
                                        className="w-100",
                                    ),
                                ],
                                className="d-flex flex-column h-100"
                            ),
                        ),
                    ],
                    style={"width": "100%"},
                ),
                width=12, md=12, lg=4, className="mb-4"
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="assets/static/turkey.png",
                            top=True,
                            style={"opacity": 0.4},
                        ),
                        dbc.CardImgOverlay(
                            dbc.CardBody(
                                [
                                    dmc.Text("🔸TBEC-2018 Response Spectrum", className="card-title fs-4"),
                                    html.Div(className="mt-auto"),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Button("Go to App", color="primary", href="/tbecresponse"),
                                                width="auto",
                                                className="ml-auto mr-auto"
                                            )
                                        ],
                                        className="w-100",
                                    ),
                                ],
                                className="d-flex flex-column h-100"
                            ),
                        ),
                    ],
                    style={"width": "100%"},
                ),
                width=12, md=12, lg=4, className="mb-4"
            ),
            
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="assets/static/usa.png",
                            top=True,
                            style={"opacity": 0.4},
                        ),
                        dbc.CardImgOverlay(
                            dbc.CardBody(
                                [
                                    dmc.Text("🔹ASCE7-22 Response Spectrum", className="card-title fs-4"),
                                    html.Div(className="mt-auto"),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Button("Go to App", color="primary", href="/asceapp"),
                                                width="auto",
                                                className="ml-auto mr-auto"
                                            )
                                        ],
                                        className="w-100",
                                    ),
                                ],
                                className="d-flex flex-column h-100"
                            ),
                        ),
                    ],
                    style={"width": "100%"},
                ),
                width=12, md=12, lg=4, className="mb-4"
            ),
            
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="assets/static/eqprocess.png",
                            top=True,
                            style={"opacity": 0.4},
                        ),
                        dbc.CardImgOverlay(
                            dbc.CardBody(
                                [
                                    dmc.Text("🌐Earthquake Data Processor", className="card-title fs-4"),
                                    html.Div(className="mt-auto"),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Button("Go to App", color="primary", href="/eqprocessor"),
                                                width="auto",
                                                className="ml-auto mr-auto"
                                            )
                                        ],
                                        className="w-100",
                                    ),
                                ],
                                className="d-flex flex-column h-100"
                            ),
                        ),
                    ],
                    style={"width": "100%"},
                ),
                width=12, md=12, lg=4, className="mb-4"
            )
            
        ], justify="start", className='mt-4 mb-4')
    ]),
    dmc.Space(h=50)  
    
])
