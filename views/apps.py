from dash import html
import sys
sys.path.append('./')
from components.navbar import navbarComponent, footerComponent
from components.gallery import galleryComponent

def layout():
    return html.Div([
    navbarComponent,
    galleryComponent,
    footerComponent
    ]) 
