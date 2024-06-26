from dash import html, dcc, callback, Output, Input, State
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import plotly.graph_objects as go
import pandas as pd
from components.navbar import navbarComponent
from applications.tbecApp.tbecResponseSpectrum import tbecTargetSpectrum

# title
tbecTitle = dmc.Text("🔸TBEC-2018 Response Spectrum Creator", className='fs-3 mx-3 mb-3 mt-3')

# create turkey hazard map
map = dl.Map([
    dl.ImageOverlay(opacity=0.5, url="\\assets\\static\\afadContour.png", bounds=[[35.65, 24.45], [42.65, 45.15]]),
    dl.TileLayer(),
    dl.LayerGroup(id="layer")
], bounds=[[35.65, 24.45], [42.65, 45.15]], style={'height': '30vh'}, id='map')

theme = dcc.Store(id='themeStore', storage_type='session')

# create default figures
# default horizontal figure
horizotanlResponseFig = go.Figure()
horizotanlResponseFig.update_xaxes(
                            title_text = 'Period (s)',
                            range = [0,3],
                        )

horizotanlResponseFig.update_yaxes(
                            rangemode =  'tozero',
                            title_text = 'pSa (g)',
                        )

horizotanlResponseFig.update_layout(showlegend=False,
                            title = 'TBEC-2018 Horizontal Response Spectrum', title_x=0.5,
                            height = 500,
                            template = "plotly_dark",
                            paper_bgcolor = "#222222",
                            plot_bgcolor = "#222222",
                            )

# default vertical figure
verticalResponseFig = go.Figure()
verticalResponseFig.update_xaxes(
                            title_text = 'Period (s)',
                            range = [0,3]
                        )

verticalResponseFig.update_yaxes(
                            rangemode =  'tozero',
                            title_text = 'pSa (g)',
                        )

verticalResponseFig.update_layout(showlegend=False, 
                            title = 'TBEC-2018 Vertical Response Spectrum', title_x=0.5,
                            height = 500,
                            template = "plotly_dark",
                            paper_bgcolor = "#222222",
                            plot_bgcolor = "#222222",
                            )

# spectral values table
defaultSpectralDict = {
    'Spectral Parameters': [
        'Spectral Acceleration Parameter at Short Periods (Ss)', 
        'Spectral Acceleration parameter at 1 sec Period (S1)', 
        'Peak Ground Acceleration (PGA)', 
        'Peak Ground Velocity (PGV)', 
        'Soil Class Coefficient for Short Period (FS)', 
        'Soil Coefficient for 1 sec Period (F1)', 
        'Design Spectral Acceleration at Short Periods (SDs)', 
        'Design Spectral Acceleration at 1 sec Period (SD1)', 
        'Spectrum Corner Period A (TA)', 
        'Spectrum Corner Period B (TB)', 
        'Spectrum Long Period (TL)', 
        'Earthquake Design Class (DTS)'],
    'Values': ['No Value']*12
}
spectralValuesFrame = pd.DataFrame(defaultSpectralDict)

spectralValuesTable = dbc.Container(
    dbc.Table.from_dataframe(
        spectralValuesFrame,
        bordered=True,
        hover=True,
        responsive=True,
        size = 'sm'
    ),style = {'textAlign': 'center'},
    className='p-2',
    id='spectralTableDiv'
)

# create input section
inputSection = html.Div(
    dbc.Row([
        # input col
        dbc.Col([
            dbc.Card(
                html.Div(
                        children = [
                            dbc.Label("Latitude", className="mb-2"),
                            dbc.Input(type = "number", id="latitudeInput", value=36.34, className="mb-2 mt-2"),
                            dbc.Label("Longitude", className="mb-2"),
                            dbc.Input(type = "number", id="longitudeInput", value=41.45, className="mb-2 mt-2"),
                            dbc.Label("Soil Type", className="mb-2 mt-2"),
                            dcc.Dropdown(id="soilTypeInput", options = ['ZA', 'ZB', 'ZC', 'ZD', 'ZE'], value = 'ZC', className="mb-2 mt-2 text-black"),
                            dbc.Label("Intensity Level", className="mb-2 mt-2"),
                            dcc.Dropdown(id="intensityLevelInput", options = ['DD1', 'DD2', 'DD3', 'DD4'], value = 'DD2', className="mb-2 mt-2 text-black"),
                            dbc.Button("Create Response Spectrum", id='responseButton', color='primary', className="mb-2 mt-2"),
                            dbc.Button("Export Data to Excel", id='exportButton', color='info', outline=True, className="mb-2 mt-2 mx-2")
                        ], className="inputArea mx-2 mb-2 mt-2"), 
                className="inputForm mx-2 mt-5")
        ], width=5),
        
        # graph col
        dbc.Col([
            dbc.Tabs(
                [
                    dbc.Tab(html.Div(dcc.Graph(figure=horizotanlResponseFig, id="horizontalFig")), label="Horizontal Response Spectrum"),
                    dbc.Tab(html.Div(dcc.Graph(figure=verticalResponseFig, id="verticalFig")), label="Vertical Response Spectrum"),
                    dbc.Tab(html.Div(spectralValuesTable), label="Spectral Values Table"),
                ],
                className='nav-fill w-100'
            )
        ], width=7)
    ], className="mx-1 mt-3")
)

def layout():
    return dmc.NotificationsProvider(
        html.Div([
            navbarComponent, 
            tbecTitle,
            map, 
            inputSection,
            dcc.Download(id="download-dataframe-xlsx"), 
            html.Div(dmc.Space(h=100)),
            html.Div(id='notificationContainer')
        ])
    )
    
# callback for styling
@callback(
    [
        Output('horizontalFig', 'figure', allow_duplicate=True), 
        Output('verticalFig', 'figure', allow_duplicate=True),
    ],
    Input('themeStore', 'data'),
    prevent_initial_call = True
)
def up(themeData):
    hFig = go.Figure(horizotanlResponseFig)
    vFig = go.Figure(verticalResponseFig)
    if themeData:
        hFig.update_layout(
            template = "plotly_white",
            paper_bgcolor = "white",
            plot_bgcolor = "white",
        )
        vFig.update_layout(
            template = "plotly_white",
            paper_bgcolor = "white",
            plot_bgcolor = "white",
        )
    else:
        hFig.update_layout(
            template = "plotly_dark",
            paper_bgcolor = "#222222",
            plot_bgcolor = "#222222",
        )
        vFig.update_layout(
            template = "plotly_dark",
            paper_bgcolor = "#222222",
            plot_bgcolor = "#222222",
        )
        
    return hFig, vFig
    
# add marker to the map
@callback(
    Output("layer", "children"),
    [Input("map", "click_lat_lng")],
)
def map_click(click_lat_lng):
    if click_lat_lng:
        marker = dl.Marker(position=click_lat_lng)
        return [marker]
    return []

# get coordinates from the click
@callback(
    [Output("latitudeInput", "value"), Output("longitudeInput", "value")],
    [Input("map", "click_lat_lng")]
)
def click_coord(click_lat_lng):
    if click_lat_lng and len(click_lat_lng) == 2:
        lat, lng = click_lat_lng
        return float(round(lat, 4)), float(round(lng, 4))
    else:
        raise PreventUpdate
    
# add functionality to response button
@callback(
    [
        Output('spectralTableDiv', 'children'),  
        Output('horizontalFig', 'figure'),  
        Output('verticalFig', 'figure')  
    ],
    Input('responseButton', 'n_clicks'),  
    [
        State('latitudeInput', 'value'),  
        State('longitudeInput', 'value'),
        State('soilTypeInput', 'value'),
        State('intensityLevelInput', 'value'),
        State('horizontalFig', 'figure'),  
        State('verticalFig', 'figure'),
        Input('themeStore', 'data'),
    ]
)
def update_spectral_values_and_figures(n_clicks, latitude, longitude, soil_type, intensity_level, horizotanlFig, verticalFig, theme):
    if not n_clicks:
        raise PreventUpdate

    returnedSpectralValues, tList, saList, sadList, spectralValuesDict = tbecTargetSpectrum(latitude, longitude, soil_type, intensity_level)
    
    if theme:
        lineColor = "#000080"
    else:
        lineColor = "#FFFF00"
        
        
    horizontalTrace = go.Scatter(x=tList, y=saList, line=dict(color=lineColor))
    verticalTrace = go.Scatter(x=tList, y=sadList, line=dict(color=lineColor))
    
    horizotanlFig['data'].append(horizontalTrace)
    verticalFig['data'].append(verticalTrace)
    
    updatedFrame = pd.DataFrame(returnedSpectralValues)
    updatedSpectralTable =  dbc.Container(
        dbc.Table.from_dataframe(
            updatedFrame,
            bordered=True,
            hover=True,
            responsive=True,
            size = 'sm'
        ),style = {'textAlign': 'center'},
        className='p-2',
    )

    return updatedSpectralTable, horizotanlFig, verticalFig

# export to excel
@callback(
    Output("download-dataframe-xlsx", "data"),
    Input("exportButton", "n_clicks"),
    [
        State('latitudeInput', 'value'),  
        State('longitudeInput', 'value'),
        State('soilTypeInput', 'value'),
        State('intensityLevelInput', 'value')
    ],
prevent_initial_call=True,
)
def func(n_clicks, latitude, longitude, soil_type, intensity_level):
    returnedSpectralValues, tList, saList, sadList, spectralValuesDict = tbecTargetSpectrum(latitude, longitude, soil_type, intensity_level)
    downloadFrame = pd.DataFrame(columns=['T', 'Sa', 'Sad'])
    downloadFrame['T'] = spectralValuesDict['T']
    downloadFrame['Sa'] = spectralValuesDict['Sa']
    downloadFrame['Sad'] = spectralValuesDict['Sad']

    return dcc.send_data_frame(downloadFrame.to_excel, "tbecResponseSpectrum.xlsx", sheet_name="Sheet_name_1")

# notification callback
@callback(
    Output("notificationContainer", "children"),
    [Input("responseButton", "n_clicks"), Input("exportButton", "n_clicks")],
    prevent_initial_call=True,
)
def show(click1, click2):
    return dmc.Notification(
                id="my-notification",
                title="Spectrum creation process initiated",
                message="Spectrum creation process has started.",
                loading=True,
                color="blue",
                action="show",
                autoClose=True,
                disallowClose=True,
            )