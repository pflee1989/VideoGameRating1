# Imports from 3rd party libraries

from joblib import load
model = load('assets/model_rf.joblib')

import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Imports from this application
from app import app


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            You Will Choose If A Particular Characteristic of Concern Is Present or Absent.
            Right below, the plot shows the strength of each selected feature within this online GradientBoost model.  
            
            You will see violence (in fantasy theme or not), bloody visuals, and languages are what set the games apart
            in game ratings. 

            As always, inapproriate languages and violence...set games apart in raing. >_<
            """
        ), 
        html.Img(src='assets/gb_online.png', className='img-fluid'),
     

        
    
    ], 
    md=3, 
    
)

column2 = dbc.Col(
    [
        
        dcc.Markdown('Fantasy Violence?'
                     ), 
        dcc.Dropdown(
            id='fantasy_violence', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0},     
            ], 
            value = '0', 
            className='mb-5'), 

        
        dcc.Markdown('Blood?'
                     ), 
        dcc.Dropdown(
            id='blood', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        
        
        dcc.Markdown('Strong Language?'
                     ), 
        dcc.Dropdown(
            id='strong_janguage', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        
        
        dcc.Markdown('Intense Violence?'
                     ), 
        dcc.Dropdown(
            id='intense_violence', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        html.H2('Game Rating', className='mb-5'), 
       
    ],
    md=4,
)

column3 = dbc.Col(
    [
        dcc.Markdown('Langauge?'
                     ), 
        dcc.Dropdown(
            id='langauge', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0},     
            ], 
            value = '0', 
            className='mb-5', 
        ), 

        dcc.Markdown('Mild Lyrics?'
                     ), 
        dcc.Dropdown(
            id='mild_lyrics', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        
        dcc.Markdown('Console?'
                     ), 
        dcc.Dropdown(
            id='console', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        
        dcc.Markdown('Suggestive Themes?'), 
        dcc.Dropdown(
            id='suggestive_themes', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 

        

    html.Div(id='prediction-content', className='lead')  
  ],
    md=4,

)

layout = dbc.Row([column1, column2, column3])


# Get the Function in
@app.callback(
Output('prediction-content', 'children'),
[Input('strong_janguage', 'value'),
 Input('fantasy_violence', 'value'), 
 Input('blood', 'value'), 
 Input('suggestive_themes', 'value'), 
 Input('intense_violence', 'value'),
 Input('language', 'value'),  
 Input('console', 'value'), 
 Input('mild_lyrics', 'value')
 ],)


def predict(strong_janguage, fantasy_violence, blood, suggestive_themes, 
            intense_violence, language, 
            console, mild_lyrics):
    df = pd.Dataframe(
        columns = ["strong_janguage", "fantasy_violence", "blood", "suggestive_themes", 
            "intense_violence", "language", 
            "console", "mild_lyrics"],
        data =[[strong_janguage, fantasy_violence, blood, suggestive_themes, 
            intense_violence, language, 
            console, mild_lyrics]]),
    y_pred = model.predict(df)[0]
    y_pred_prob= model.predict_proba(df)
    E = round(y_pred_prob[0][0]*100, 2)
    ET = round(y_pred_prob[0][1]*100, 2)
    T = round(y_pred_prob[0][2]*100, 2)
    M = round(y_pred_prob[0][3]*100, 2)
    prob =  round(y_pred_prob[0], 2)*100
    if y_pred == 'E':
        return """{}: {}% |
                 \nET: {}% |
                 \nT: {}% | 
                 \nM: {}%  
            """.format(y_pred, E, ET, T, M)
    if y_pred == 'ET':
        return """E: {}% | 
                  \n{}: {}% |  
                  \nT: {}% |  
                  \nM: {}%    
            """.format(E, y_pred, ET, T, M)
    if y_pred == "T":
        return """E: {}% | 
                \nET: {}% | 
                \n{}: {}% | 
                \nM: {}%   
            """.format( E, ET, y_pred, T, M)
    if y_pred == "M":
        return """E: {}% | 
                \nET: {}% | 
                \nT: {}% | 
                \n{}: {}%   
            """.format(E, ET, T, y_pred, M)
