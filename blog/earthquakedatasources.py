from dash import html, dcc
import sys
import dash_mantine_components as dmc
sys.path.append('./')
from components.navbar import navbarComponent, footerComponent

body = html.Div(className="col-12 col-md-12 mt-4 text-center", children=[
                dcc.Markdown('''

                    ## Earthquake Data Sources
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                    Praesent viverra nisi at nisi ultricies, at dapibus felis pretium. 
                    Suspendisse potenti. Integer in ex vitae augue vehicula consectetur.
                ''')
            ])

def layout():
    return html.Div([
        navbarComponent,
        body,
        footerComponent
    ])
