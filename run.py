# Imports from 3rd party libraries

# from joblib import load
# pipeline = load('assets/pipeline_joblib')
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predictions, insights, process

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Video Game Rating: E, ET, T, M',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/Predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Insights', href='/Insights', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/Process', className='nav-link')),
        # dbc.NavItem(dcc.Link('Result', href='/Result', className='nav-link')) 
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Philip Lee', className='mr-2'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/pflee/'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:pflee1989@outlook.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/pflee1989/VideoGameRating1.git'), 
                    html.A(html.I(className='fab fa-medium'), href='https://philipfeiranlee.medium.com/video-game-rating-trying-to-simulate-whats-in-the-head-of-the-raters-165c6cf73d16'), 
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/Predictions':
        return predictions.layout
    elif pathname == '/Insights':
        return insights.layout
    elif pathname == '/Process':
        return process.layout
    # elif pathname == '/Result':
    #     return Result.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)