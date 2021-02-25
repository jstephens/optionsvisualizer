import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from yahoo_fin import options

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['TSLA', 'MSFT']],
        value='MSFT'
    ),
    html.Div(id='display-value'),
    html.Div(id='display-dates')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

def display_dates(value):
    stock_dates = options.get_expiration_dates(value)
    return stock_dates

if __name__ == '__main__':
    app.run_server(debug=True)