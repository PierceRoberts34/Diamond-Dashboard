from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/tidyverse/ggplot2/refs/heads/main/data-raw/diamonds.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    html.Div([html.Div([html.H1([
        html.Span("Welcome"),
        html.Br(),
        html.Span("to the diamond dashboard!")
    ]),
    html.P("This classic dataset contains the prices and other attributes of almost 54,000 diamonds. It's a great dataset for beginners learning to work with data analysis and visualization.")
],
    style={
        "vertical-alignment": "top",
        "height": 260
    }), html.Div([
        html.Div(dbc.RadioItems(
            id='radio',
            className='btn-group',
            inputClassName='btn-check',
            labelClassName="btn btn-outline-light",
            labelCheckedClassName="btn btn-light",
            options=[
                {"label": "Count", "value": 1}, 
                {"label": "Violin", "value": 2},
                {"label": "Price", "value": 3}
            ],
            value=1
        ),
                 style={'width': 300})
    ],
    style={
        'margin-left': 15,
        'margin-right': 15,
        'display': 'flex'
    }),
              html.Div(), html.Div()],
             style={
                 'width': 340,
                 'margin-left': 35,
                 'margin-top': 35,
                 'margin-bottom': 35
             }),
    html.Div(
        [html.Div(dcc.Graph(id='graph'),style={'width': 790}),
         html.Div(style={'width': 200})],
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35,
            'display': 'flex'
        })
],
    fluid=True,
    style={'display': 'flex'},
    className='dashboard-container')

# Create graphs
@app.callback(
    Output("graph", "figure"),
    Input("radio", 'value'))
def display_graph(value):
    if value == 1:
        fig = px.histogram(
            df,
            x = "cut",
            category_orders= {"cut":["Fair", "Good", "Very Good", "Premium", "Ideal"]}
        )
    elif value == 2:
        fig = px.violin(
            df,
            x = "cut",
            y = "price",
            category_orders= {"cut":["Fair", "Good", "Very Good", "Premium", "Ideal"]}
        )
    else:
        fig = px.histogram(
            df,
            x = "price",
            facet_col = "cut",
            facet_col_wrap=3,
            category_orders= {"cut":["Fair", "Good", "Very Good", "Premium", "Ideal"]},
            histnorm = 'percent'
        )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
