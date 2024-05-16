from dash import html
import dash_mantine_components as dmc

def layout():
    return html.Div([
        "This is the HOME",
        dmc.Anchor(href="/apps", children=["Go To App"]),

        
    ]) 
