# Imports from 3rd party libraries
# import joblib
from joblib import load
pipeline = load('assets/pipeline_joblib')
# a copy of the filepath (r'C:\Users\pflee\Desktop\Local Work\Video-Game-Rating-Formal\Video-Game-Rating\assets\pipline_joblib')
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# from joblib import load
# pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app


# Get the Function in
@app.callback(
Output('prediction-content', 'children'),
[Input('strong_janguage', 'value'), Input('no_descriptors', 'value'), Input('mild_fantasy_violence', 'value'), Input('blood_and_gore', 'value'), Input('blood', 'value'), Input('strong_sexual_content', 'value')],
# [Input('blood_and_gore', 'value'), Input('strong_janguage', 'value')],
# [Input('strong_sexual_content', 'value'), Input('mild_fantasy_violence', 'value')]
)
# Order of the Variables in the App Version
# strong_janguage	no_descriptors	mild_fantasy_violence	blood_and_gore	blood	strong_sexual_content
def predict(strong_janguage, no_descriptors, 
            mild_fantasy_violence, blood_and_gore, blood, 
            strong_sexual_content):
    # print(strong_janguage)
    df = pd.Series(
        # columns = ["strong_janguage", "no_descriptors", 
        #     "blood", "mild_fantsy_violence", 
        #     "blood_and_gore",  "strong_sexual_content"],
        data =[strong_janguage, no_descriptors, 
            mild_fantasy_violence, blood_and_gore, blood, 
            strong_sexual_content]),
    y_pred = pipeline.predict(df)[0]
    y_pred_prob= pipeline.predict_proba(df)[0]
    prob =  100 - (round(y_pred_prob[0], 2))*100
    # print(y_pred)
    return "The game is {}% likely to receive a {} rating.".format(prob, y_pred) 



# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            You Will Choose If A Particular Characteristic of Concern Is Present or Absent.
            On the right, the plot shows the strength of each variable within this online GradientBoost model.  
            
            You will see that strong langauge is the most important indicator of maturity necessary for the game content. 
            Blood and gore, blood, mild fantasy violence and no decriptor follow. 


            As always, strong languages tend to be inappropriate >_<
            """
        ), 
        html.Img(src='assets/GBC Important Features.png', className='img-fluid'),
     

        
    
    ], 
    md=4, 
    
)

column2 = dbc.Col(
    [
             dcc.Markdown('Strong Language?'
                     ), 
        dcc.Dropdown(
            id='strong_janguage', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0},     
            ], 
            value = '0', 
            className='mb-5', 
        ), 
        # !/usr/bin/python3
           dcc.Markdown('No Decription of the Content?'
                     ), 
        dcc.Dropdown(
            id='no_descriptors', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        #     dcc.Markdown('Fantasy Violence?'
        #              ), 
        # dcc.Dropdown(
        #     id='fantasy_violence', 
        #     options = [
        #         {'label': 'Yes', 'value': '1'}, 
        #         {'label': 'No', 'value': '0'}, ], 
        #     value = 'Fantasy Violence', 
        #     className='mb-5', 
        # ), 
        
               dcc.Markdown('Blood and Gore?'
                     ), 
        dcc.Dropdown(
            id='blood_and_gore', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        html.H2('Game Rating', className='mb-5'), 
        
        #           dcc.Markdown('Mild Cartoon Violence?'
        #              ), 
        # dcc.Dropdown(
        #     id='mild_cartoon_violence', 
        #     options = [
        #         {'label': 'Yes', 'value': '1'}, 
        #         {'label': 'No', 'value': '0'}, ], 
        #     value = 'Mild Cartoon Violence', 
        #     className='mb-5', 
        # ), 
      
   
      
        
    ],
    md=4,
)

column3 = dbc.Col(
    [
             dcc.Markdown('Blood?'
                     ), 
        dcc.Dropdown(
            id='blood', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0},     
            ], 
            value = '0', 
            className='mb-5', 
        ), 
        # !/usr/bin/python3
           dcc.Markdown('Mild Fantasy Violence?'
                     ), 
        dcc.Dropdown(
            id='mild_fantasy_violence', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        #     dcc.Markdown('Violence?'
        #              ), 
        # dcc.Dropdown(
        #     id='violence', 
        #     options = [
        #         {'label': 'Yes', 'value': '1'}, 
        #         {'label': 'No', 'value': '0'}, ], 
        #     value = 'Violence', 
        #     className='mb-5', 
        # ), 
        
               dcc.Markdown('Strong Sexual Content?'
                     ), 
        dcc.Dropdown(
            id='strong_sexual_content', 
            options = [
                {'label': 'Yes', 'value': 1}, 
                {'label': 'No', 'value': 0}, ], 
            value = '0', 
            className='mb-5', 
        ), 
        #   dcc.Markdown('Cartoon Violence?'
        #              ), 
        # dcc.Dropdown(
        #     id='cartoon_violence', 
        #     options = [
        #         {'label': 'Yes', 'value': '1'}, 
        #         {'label': 'No', 'value': '0'}, ], 
        #     value = 'Cartoon Violence', 
        #     className='mb-5', 
        # ), 
        
#  dcc.Link(dbc.Button('Get Your Game Rating', color='primary'), href='/Result')
    html.Div(id='prediction-content', className='lead')  
  ],
    md=4,
# column4 = dbc.Col(
#     [
#     ]
)

layout = dbc.Row([column1, column2, column3])