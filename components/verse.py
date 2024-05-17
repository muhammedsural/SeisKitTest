import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_extensions as de

verseComponent = html.Div([


    dmc.Divider(style={'backgroundColor': '#333333', 'opacity': '0.5'}, className='mx-5 mt-5 mb-5'),

    
    dbc.Row(
            [
            dbc.Col(
                [
                    html.Div([
                        html.Div([dmc.Image(src="assets/static/webapp.svg", width="80%", className="d-none d-lg-block")])
                    ])
                ], className='mt-5',
                xs=10, sm=10, md=10, lg=4, xl=4),
            
            dbc.Col([
                        html.Div([
                            html.Div(dmc.Text("Web Applications", className="fs-2")),
                            dmc.Space(h=30),
                            html.Div(dmc.Text("Easy access to the web applications developed by the earthquake and structural engineering community.", className="fs-6")),
                            dmc.Space(h=30),
                            html.Div(dmc.Text("No Login. No Subscription.", className="fs-6")),
                            dmc.Space(h=30),
                            html.Div([
                                dbc.Button("Go to Applications", outline=True, color="primary", id="applicationsButton", href='/apps'),
                                ], className="d-grid gap-2 d-md-flex justify-content-md-start")
                        ], 
                        className='mt-3'),
                    ], 
                    xs=10, sm=10, md=10, lg=4, xl=4),
            ],
            justify="center",
            className='g-0'
        ),
    
    dmc.Space(h=50),
    
    dbc.Row(
            [
                
            dbc.Col([
                        html.Div([
                            html.Div(dmc.Text("Open-Source", className="fs-2")),
                            dmc.Space(h=30),
                            html.Div(dmc.Text("Transparent and well-documented theory for the applications.", className="fs-6")),
                            dmc.Space(h=30),
                            html.Div(dmc.Text("Open to contribution in public GitHub repository.", className="fs-6")),
                            dmc.Space(h=30),
                            html.Div([
                                dbc.Button("Go to Source Code", outline=True, color="primary", id="sourceCodeButton", href='https://github.com/dogukankaratas/SeisKit', target='_blank'),
                                ], className="d-grid gap-2 d-md-flex justify-content-md-start")
                        ], 
                        className='mt-3'),
                    ], 
                    xs=10, sm=10, md=10, lg=4, xl=4),
            
            dbc.Col(
                [
                    html.Div([
                        html.Div([dmc.Image(src="assets\static\public.png", width="80%", className="d-none d-lg-block")])
                    ])
                ], className='mt-5 ml-5',
                xs=10, sm=10, md=10, lg=4, xl=4),
            
            
            ],
            justify="center",
            className='g-0'
        ),
    
    dmc.Space(h=50),
    
    dbc.Row(
            [
            dbc.Col(
                [
                    html.Div([
                        html.Div([dmc.Image(src="assets/static/team.svg", width="80%", className="d-none d-lg-block")])
                    ])
                ], className='mt-5',
                xs=10, sm=10, md=10, lg=4, xl=4),
            
            dbc.Col([
                        html.Div([
                            html.Div(dmc.Text("Community Driven", className="fs-2")),
                            dmc.Space(h=30),
                            html.Div(dmc.Text("Get in touch with the app creators and other users.", className="fs-6")),
                            dmc.Space(h=30),
                            html.Div(dmc.Text("Join our Slack group.", className="fs-6")),
                            dmc.Space(h=30),
                            html.Div([
                                dbc.Button("Join Slack", outline=True, color="primary", id="sourceCodeButton", href='https://join.slack.com/t/seiskit/shared_invite/zt-2bb7zi6f4-d6E~TJ9QmBfNutV6bEmNHA', target='_blank'),
                                ], className="d-grid gap-2 d-md-flex justify-content-md-start")
                        ], 
                        className='mt-3'),
                    ], 
                    xs=10, sm=10, md=10, lg=4, xl=4),
            ],
            justify="center",
            className='g-0'
        ),
    
    dmc.Space(h=100),
])