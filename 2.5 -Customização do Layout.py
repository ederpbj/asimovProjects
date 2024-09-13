import dash
from dash import html, dcc
from plotly.express import data

import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# ================> Layout
app.layout = html.Div([
    html.Label("Dropdown"),

    dcc.Dropdown(
        id="dp-1",
        options=[{'label': 'Rio Grande do Sul', 'value':'RS'},
                 {'label':'Sao Paulo', 'value':'SP'},
                 {'label':'Parana', 'value':'PR'},
        ],
        value='PR', style={"margin-bottom": "25px"}
    ),

    html.Div([
        html.Label("Checklist"),
        dcc.Checklist(
            id="cl-1",
            options=[{'label': 'Rio Grande do Sul', 'value': 'RS'},
                     {'label': 'Sao Paulo', 'value': 'SP'},
                     {'label': 'Parana', 'value': 'PR'}],
            value=['PR']
        ),

        html.Label('Text Input'),
        dcc.Input(value='SP', type='text'),

        dcc.Slider(min=0, max=20, step=5, value=10, id='my-slider'),

        dcc.Slider(0, 10,
            step=None,
            marks={
                0: '0°C',
                3: '3°F',
                5: '5°F',
                7.65: '7.65°F',
                10: '10°F'
            },
            value=5
        )
    ])
])



# sempre no fim do projeto colocar:
if __name__ == '__main__':
  app.run_server(debug=True)
