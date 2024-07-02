from dash import Dash, html, dcc, callback, Output, Input
from views import about, home, apps, blog
from blog import seisscalelogic, earthquakedatasources
from applications.tbecApp import tbecApp
from applications.seisScale import seisScale
from applications.eqProcessor import eqProcessor
from applications.asceApp import asceApp

app = Dash(__name__, suppress_callback_exceptions=True)
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
    elif pathname == '/blog':
        return blog.layout()
    elif pathname == '/about':
        return about.layout()
    elif pathname == '/seisscalelogic':
        return seisscalelogic.layout()
    elif pathname == '/earthquakedatasources':
        return earthquakedatasources.layout()
    
if __name__ == '__main__':
    app.run_server(debug=True)
