from dash import html
import sys
sys.path.append('./')
from components.navbar import navbarComponent, footerComponent
from components.header import headerComponent
from components.verse import verseComponent

def layout():
    return html.Div([
    navbarComponent,
    headerComponent,
    verseComponent,
    footerComponent
    ]) 
