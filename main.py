from dash import Dash, html, dcc, callback, Output, Input
from views import home, apps
from applications.tbecApp import tbecApp
from applications.seisScale import seisScale
from applications.eqProcessor import eqProcessor
from applications.asceApp import asceApp

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='themeStore', storage_type='session'),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout()
    elif pathname == '/':
        return home.layout()
    elif pathname == '/apps':
        return apps.layout()
    elif pathname == '/tbecresponse':
        return tbecApp.layout()
    elif pathname == '/seisscale':
        return seisScale.layout()
    elif pathname == '/asceapp':
        return asceApp.layout()
    elif pathname == '/eqprocessor':
        return eqProcessor.layout()
    
if __name__ == '__main__':
    app.run_server(debug=True)
