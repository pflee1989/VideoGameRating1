import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

print(dcc.__version__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True

index_page = html.Div(
    # I added this id attribute
    id='index_page',
    children=[
                dcc.Link('Go to Page 1', href='/page-1'),
                html.Br(),
                dcc.Link('Go to Page 2', href='/page-2'),
            ],
    # I added this style attribute
    style={'display': 'block', 'line-height':'0', 'height': '0', 'overflow': 'hidden'}
)

page_1_layout = html.Div(
    # I added this id attribute
    id='page_1_layout',
    children=[
        html.H1('Page 1'),
        dcc.Dropdown(
            id='page-1-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='page-1-content'),
        html.Br(),
        dcc.Link('Go to Page 2', href='/page-2'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ],
    # I added this style attribute
    style={'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden'}

)

page_2_layout = html.Div(
    # I added this id attribute
    id='page_2_layout',
    children=[
        html.H1('Page 2'),
        html.Div(id='page-2-content'),
        html.Br(),
        dcc.Link('Go to Page 1', href='/page-1'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ],
    # I added this style attribute
    style={'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden'}
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',
             # I added this children attribute
             children=[index_page, page_1_layout, page_2_layout]
             )
])


# Update the index
@app.callback(
    [dash.dependencies.Output(page, 'style') for page in ['index_page', 'page_1_layout', 'page_2_layout']],
    # I turned the output into a list of pages
    [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return_value = [{'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden'} for _ in range(3)]

    if pathname == '/page-1':
        return_value[1] = {'height': 'auto', 'display': 'inline-block'}
        return return_value
    elif pathname == '/page-2':
        return_value[2] = {'height': 'auto', 'display': 'inline-block'}
        return return_value
    else:
        return_value[0] = {'height': 'auto', 'display': 'inline-block'}
        return return_value


@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


@app.callback(Output('page-2-content', 'children'),
              [Input('page-1-dropdown', 'value')])
def page_2(value):
    return 'You selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True, port=1244, host='0.0.0.0')