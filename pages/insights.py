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
        
            ## Insights
            This model is realistic, but less powerful than the complete one because this model only used 10 features. The picture below shows the important features of the original model. 
            For the complete model is completely different. Please refer to the 
            notebook through the github icon, or the blog post through the medium icon. 

            """
        
        ), 
    
    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

    html.Img(src='assets/XGBoost All Features.png', className='img-fluid')
    
    ],
)



       
layout = dbc.Row([column1])