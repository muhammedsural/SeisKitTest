from dash import Dash, html, dcc, callback, Output, Input
from views import home, apps

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
    
if __name__ == '__main__':
    app.run_server(debug=True)
