import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, callback
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import plotly.graph_objects as go
import dash_leaflet as dl
import pandas as pd
from components.navbar import navbarComponent
from applications.asceApp.accessAsce import getAsceDataMulti, getAsceDataMultiMCEr, getAsceDataTwo, getAsceDataTwoMCEr

# title
asceTitle = dmc.Text("🔹ASCE7-22 Response Spectrum", className='fs-3 mx-3 mb-3 mt-3')

# create usa hazard map
map = dl.Map([
    dl.ImageOverlay(opacity=0.7, url="\\assets\\static\\usaHazard.png", bounds=[[22.8, -129.2], [50.5, -62.9]]),
    dl.TileLayer(),
    dl.LayerGroup(id="asceLayer")
], center=[38.63, -100], zoom=3, style={'height': '30vh'}, id='usaMap', className="usaMap")

inputSection = html.Div([
    dbc.Card(html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Label("Latitude", className="mx-3 mt-2"),
                        dbc.Input(type = "number", id="asceLatitudeInput", value=37.81, className="mb-2 mt-2 mx-2")
            ]),
            dbc.Col([
                dbc.Label("Longitude", className="mx-3 mt-2"),
                        dbc.Input(type = "number", id="asceLongitudeInput", value=-122.47, className="mb-2 mt-2 mx-2")
            ]),
            dbc.Col([
                dbc.Label("Site Category", className="mx-3 mt-2"),
                dcc.Dropdown(id="asceSiteCategoryInput", options = ['A', 'B', 'C', 'D', 'E'], value = 'C', className="mb-2 mt-2 mx-2 text-black"),
            ]),
        ]),
        dbc.Row([
            dbc.Col(md=4, lg=4),
            dbc.Col([
                dbc.Button("Create Response Spectrum", id='asceResponseButton', color='primary', className="mb-2 mt-2 mx-2"),
                dbc.Button("Export Data to Excel", id='asceExportButton', color='info', outline=True, className="mb-2 mt-2 mx-2")

            ], md=4, lg=4, className='text-center'), 
            dbc.Col(md=4, lg=4), 
        ])
    ]), className="mx-3 mt-3")
])

# default graphs
multiPeriodFig = go.Figure()
multiPeriodFig.update_xaxes(
                        title_text = 'Period (s)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

multiPeriodFig.update_yaxes(
                        title_text = 'pSa (g)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

multiPeriodFig.update_layout(showlegend=False, 
                                title = 'ASCE7-22 Multi Period Design Spectrum', title_x=0.5,
                                template = "plotly_dark",
                                paper_bgcolor = "#222222",
                                plot_bgcolor = "#222222",
                            )

multiPeriodMcerFig = go.Figure()
multiPeriodMcerFig.update_xaxes(
                        title_text = 'Period (s)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

multiPeriodMcerFig.update_yaxes(
                        title_text = 'pSa (g)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

multiPeriodMcerFig.update_layout(showlegend=False, 
                                title = 'ASCE7-22 Multi Period MCEr Design Spectrum', title_x=0.5,
                                template = "plotly_dark",
                                paper_bgcolor = "#222222",
                                plot_bgcolor = "#222222",
                            )

twoPeriodFig = go.Figure()
twoPeriodFig.update_xaxes(
                        title_text = 'Period (s)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

twoPeriodFig.update_yaxes(
                        title_text = 'pSa (g)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

twoPeriodFig.update_layout(
                            showlegend=False, 
                            title = 'ASCE7-22 Two Period Design Spectrum', title_x=0.5,
                            template = "plotly_dark",
                            paper_bgcolor = "#222222",
                            plot_bgcolor = "#222222",
                        )

twoPeriodMcerFig = go.Figure()
twoPeriodMcerFig.update_xaxes(
                        title_text = 'Period (s)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

twoPeriodMcerFig.update_yaxes(
                        title_text = 'pSa (g)',
                        rangemode =  'tozero',
                        showgrid = True,
                        showline = True,
                    )

twoPeriodMcerFig.update_layout(showlegend=False,
                                title = 'ASCE7-22 Two Period MCEr Design Spectrum', title_x=0.5,
                                template = "plotly_dark",
                                paper_bgcolor = "#222222",
                                plot_bgcolor = "#222222",
                            )

graphSection = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='multiPeriodFig', figure=multiPeriodFig, className='mx-3 mb-3 mt-3'),
            dcc.Graph(id='twoPeriodFig', figure=twoPeriodFig, className='mx-3 mb-3 mt-3')
        ], width=6),
        dbc.Col([
            dcc.Graph(id='multiPeriodMcerFig', figure=multiPeriodMcerFig, className="mx-3 mb-3 mt-3"),
            dcc.Graph(id='twoPeriodMcerFig', figure=twoPeriodMcerFig, className="mx-3 mb-3 mt-3")
        ], width=6)
    ]),
], style={'overflow': 'hidden'})

def layout():
    return[
        navbarComponent,
        asceTitle,
        map,
        inputSection,
        graphSection
    ]
        
# add marker to the map
@callback(
    Output("asceLayer", "children"),
    [Input("usaMap", "click_lat_lng")],
)
def map_click(click_lat_lng):
    if click_lat_lng:
        marker = dl.Marker(position=click_lat_lng)
        return [marker]
    return []
    
# get coordinates from the click
@callback(
    [Output("asceLatitudeInput", "value"), Output("asceLongitudeInput", "value")],
    [Input("usaMap", "click_lat_lng")]
)
def click_coord(click_lat_lng):
    if click_lat_lng and len(click_lat_lng) == 2:
        lat, lng = click_lat_lng
        return float(round(lat, 4)), float(round(lng, 4))
    else:
        raise PreventUpdate
    
# update graphs
@callback(
    [
        Output('multiPeriodFig', 'figure'),
        Output('multiPeriodMcerFig', 'figure'),
        Output('twoPeriodFig', 'figure'),
        Output('twoPeriodMcerFig', 'figure')
    ],
        Input('asceResponseButton', 'n_clicks'),
    [
        State('asceLatitudeInput', 'value'),
        State('asceLongitudeInput', 'value'),
        State('asceSiteCategoryInput', 'value'),
        State('multiPeriodFig', 'figure'),
        State('multiPeriodMcerFig', 'figure'),
        State('twoPeriodFig', 'figure'),
        State('twoPeriodMcerFig', 'figure'),
        Input('themeStore', 'data')
    ]
)
def updateGraphs(n_clicks, latitude, longitude, siteCategory, upMulti, upMultiMcer, upTwo, upTwoMcer, theme):
    if not n_clicks:
        raise PreventUpdate
    
    # clean the graph
    upMulti['data'] = []
    upMultiMcer['data'] = []
    upTwo['data'] = []
    upTwoMcer['data'] = []

    if theme:
        upMulti['layout']['paper_bgcolor'] = 'white'
        upMulti['layout']['plot_bgcolor'] = 'white'
        upMulti['layout']['template'] = 'plotly_white'
        
        upMultiMcer['layout']['paper_bgcolor'] = 'white'
        upMultiMcer['layout']['plot_bgcolor'] = 'white'
        upMultiMcer['layout']['template'] = 'plotly_white'
        
        upTwo['layout']['paper_bgcolor'] = 'white'
        upTwo['layout']['plot_bgcolor'] = 'white'
        upTwo['layout']['template'] = 'plotly_white'
        
        upTwoMcer['layout']['paper_bgcolor'] = 'white'
        upTwoMcer['layout']['plot_bgcolor'] = 'white'
        upTwoMcer['layout']['template'] = 'plotly_white'
        
        lineColor = "#000080"
    else:
        upMulti['layout']['paper_bgcolor'] = '#222222'
        upMulti['layout']['plot_bgcolor'] = '#222222'
        
        upMultiMcer['layout']['paper_bgcolor'] = '#222222'
        upMultiMcer['layout']['plot_bgcolor'] = '#222222'
        
        upTwo['layout']['paper_bgcolor'] = '#222222'
        upTwo['layout']['plot_bgcolor'] = '#222222'
        
        upTwoMcer['layout']['paper_bgcolor'] = '#222222'
        upTwoMcer['layout']['plot_bgcolor'] = '#222222'

        
        lineColor = "#FFFF00"
       
    multiData = getAsceDataMulti(latitude, longitude, 'III', siteCategory, 'Call')
    multiMcerData = getAsceDataMultiMCEr(latitude, longitude, 'III', siteCategory, 'Call')
    twoPeriodData = getAsceDataTwo(latitude, longitude, 'III', siteCategory, 'Call')
    twoPeriodMcerData = getAsceDataTwoMCEr(latitude, longitude, 'III', siteCategory, 'Call')
    
    multiTrace = go.Scatter(
                    x = multiData['multiPeriodDesignSpectrumPeriods'],
                    y = multiData['multiPeriodDesignSpectrumOrdinates'],
                    line=dict(color=lineColor))
    
    multiMcerTrace = go.Scatter(
                    x = multiMcerData['multiPeriodMCErSpectrumPeriods'],
                    y = multiMcerData['multiPeriodMCErSpectrumOrdinates'],
                    line=dict(color=lineColor))
    
    twoTrace = go.Scatter(
                    x = twoPeriodData['twoPeriodDesignSpectrumPeriods'],
                    y = twoPeriodData['twoPeriodDesignSpectrumOrdinates'],
                    line=dict(color=lineColor))
    
    twoMcerTrace = go.Scatter(
                    x = twoPeriodMcerData['twoPeriodMCErSpectrumPeriods'],
                    y = twoPeriodMcerData['twoPeriodMCErSpectrumOrdinates'],
                    line=dict(color=lineColor))
    
    upMulti['data'].append(multiTrace)
    upMultiMcer['data'].append(multiMcerTrace)
    upTwo['data'].append(twoTrace)
    upTwoMcer['data'].append(twoMcerTrace)

    return upMulti, upMultiMcer, upTwo, upTwoMcer

@callback(
    [
        Output('multiPeriodFig', 'figure', allow_duplicate=True),
        Output('multiPeriodMcerFig', 'figure', allow_duplicate=True),
        Output('twoPeriodFig', 'figure', allow_duplicate=True),
        Output('twoPeriodMcerFig', 'figure', allow_duplicate=True)
    ],
    Input('themeStore', 'data'),
    prevent_initial_call = True
)
def updateStyle(themeData):
    multiFig = go.Figure(multiPeriodFig)
    multiMcerFig = go.Figure(multiPeriodMcerFig)
    twoFig = go.Figure(twoPeriodFig)
    twoMcerFig = go.Figure(twoPeriodMcerFig)
    
    if themeData:
        multiFig.update_layout(
            template = "plotly_white",
            paper_bgcolor = "white",
            plot_bgcolor = "white",
        )
        multiMcerFig.update_layout(
            template = "plotly_white",
            paper_bgcolor = "white",
            plot_bgcolor = "white",
        )
        twoFig.update_layout(
                template = "plotly_white",
                paper_bgcolor = "white",
                plot_bgcolor = "white",
            )
        twoMcerFig.update_layout(
                template = "plotly_white",
                paper_bgcolor = "white",
                plot_bgcolor = "white",
            )
    else:
        multiFig.update_layout(
            template = "plotly_dark",
            paper_bgcolor = "#222222",
            plot_bgcolor = "#222222",
        )
        multiMcerFig.update_layout(
            template = "plotly_dark",
            paper_bgcolor = "#222222",
            plot_bgcolor = "#222222",
        )
        twoFig.update_layout(
                template = "plotly_dark",
                paper_bgcolor = "#222222",
                plot_bgcolor = "#222222",
            )
        twoMcerFig.update_layout(
                template = "plotly_dark",
                paper_bgcolor = "#222222",
                plot_bgcolor = "#222222",
            )
        
        
    return multiFig, multiMcerFig, twoFig, twoMcerFig