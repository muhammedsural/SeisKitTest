from dash import html
import dash_mantine_components as dmc
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

def layout():
    return html.Div([
        html.H1(children='Title of Dash App', style={'textAlign':'center'}),
        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
        dcc.Graph(id='graph-content'),
        dmc.Anchor(href="/home", children=["Go To Home"]),
    ]) 

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')