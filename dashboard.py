from parametros import encuesta
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State

app = Dash(__name__)

# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div([
    html.Div(children=[
        html.Br(),
        html.Label(encuesta['Pregunta 1']['text']),
        dcc.Dropdown(encuesta['Pregunta 1']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 2']['text']),
        dcc.Dropdown(encuesta['Pregunta 2']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 3']['text']),
        html.Br(),
        dcc.Input(value='Ingrese un valor', type='text'),


        html.Br(),
        html.Br(),
        html.Label(encuesta['Pregunta 4']['text']),
        dcc.Dropdown(encuesta['Pregunta 4']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 5']['text']),
        dcc.Dropdown(encuesta['Pregunta 5']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 6']['text']),
        dcc.Dropdown(encuesta['Pregunta 6']['opc'])

    ], style={'width':550}),

    html.Div(children=[html.Br(),
        html.Label(encuesta['Pregunta 7']['text']),
        dcc.Dropdown(encuesta['Pregunta 7']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 8']['text']),
        dcc.Dropdown(encuesta['Pregunta 8']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 9']['text']),
        dcc.Dropdown(encuesta['Pregunta 9']['opc']),

        html.Br(),
        html.Label(encuesta['Pregunta 10']['text']),
        dcc.Dropdown(encuesta['Pregunta 10']['opc']),

    ], style={'padding': 5, 'width':550, 'margin-left':40})
], style={'display': 'flex', 'flex-direction': 'row', 'marginTop': 40, 'margin-right':40, 'font-size':20, 'font-family':'helvetica'})

if __name__ == '__main__':
    app.run_server(debug=True)