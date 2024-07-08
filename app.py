from dash import Dash, html, dcc, callback, Output, Input
from views import about, home, apps, blog
from blog import seisscalelogic, earthquakedatasources
from applications.tbecApp import tbecApp
from applications.seisScale import seisScale
from applications.eqProcessor import eqProcessor
from applications.asceApp import asceApp
import time
import uuid

app = Dash(__name__, suppress_callback_exceptions=True, title="SeisKit")
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    dcc.Store(id='themeStore', storage_type='session'),
    html.Div(id='page-content'),
    html.Script('''
        (function() {
            var currentPathname = window.location.pathname;
            window.addEventListener('popstate', function(event) {
                if (currentPathname !== window.location.pathname) {
                    window.location.reload();
                }
            });
        })();
    ''')
])

@callback(Output('page-content', 'children'),
          [Input('url', 'pathname')])
def display_page(pathname):
    unique_key = str(uuid.uuid4())  # Generate a unique key
    if pathname == '/home':
        content = home.layout()
    elif pathname == '/':
        content = home.layout()
    elif pathname == '/apps':
        content = apps.layout()
    elif pathname == '/tbecresponse':
        content = tbecApp.layout()
    elif pathname == '/seisscale':
        content = seisScale.layout()
    elif pathname == '/asceapp':
        content = asceApp.layout()
    elif pathname == '/eqprocessor':
        content = eqProcessor.layout()
    elif pathname == '/blog':
        content = blog.layout()
    elif pathname == '/about':
        content = about.layout()
    elif pathname == '/seisscalelogic':
        content = seisscalelogic.layout()
    elif pathname == '/earthquakedatasources':
        content = earthquakedatasources.layout()
    else:
        content = '404 Page Not Found'

    return html.Div(content, key=unique_key)  # Use the unique key here

if __name__ == '__main__':
    app.run_server(debug=True)
