import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import html
import dash_extensions as de

headerComponent = html.Div(
    dbc.Row(
            [
            dbc.Col(
                [
                    html.Div(dmc.Text("Web Applications for Earthquake Engineering", className='fs-2')),
                    dmc.Space(h=30),
                    html.Div(dmc.Text("Quickly access community-driven developed earthquake"), className = 'fs-6'),
                    html.Div(dmc.Text("engineering web applications.")),
                    dmc.Space(h=30),
                    html.Div(dmc.Text("For free.", className = 'fs-6')),
                    dmc.Space(h=30),
                    html.Div([
                    dbc.Button("Go to Applications", outline=True, color="primary", id="applicationsButton", href='/apps'),
                    dbc.Button("Go to Source Code", outline=True, color="primary", id="sourceCodeButton", href='https://github.com/dogukankaratas/SeisKit', target='_blank'),
                    ], className="d-grid gap-2 d-md-flex justify-content-md-start")
                ], className='mt-5',
                xs=10, sm=10, md=10, lg=4, xl=4),
            
            dbc.Col([
                        html.Div([
                            de.Lottie(
                                options=dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice')),
                                width = "75%",
                                url=r"assets\static\animation.json",
                            )
                        ], 
                        className='mt-5 d-none d-lg-block'),
                    ], 
                    xs=10, sm=10, md=10, lg=4, xl=4),
            ],
            justify="center",
            className='g-0'
        ),
)
