# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            Please visit my blog per the medium icon at the bottom, or this link:
            
            https://philipfeiranlee.medium.com/video-game-rating-trying-to-simulate-whats-in-the-head-of-the-raters-165c6cf73d16

            """
        ),
        html.Img(src='assets/esrb_ratings.png', className='img-fluid'),
    ],
    
)

layout = dbc.Row([column1])