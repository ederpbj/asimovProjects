import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# ===> Layout
app.layout = html.Div([
  html.H6("Altere o valor abaixo para ver callback em acao!"),
  html.Div(["Entrada:",
            dcc.Input(id='my-input', value='Valor inicial', type='text')]),
  html.Br(),

  # componente a ser alterado
  html.Div(id='my-output'),
])

@app.callback(
  Output(component_id="my-output", component_property="children"), # componente a ser alterado
  Input(component_id="my-input", component_property="value") # componente linkado
)

# função de alteração chamada
def update_output_div(value):
  return "Saida: {}".format(value)


# sempre no fim do projeto colocar:
if __name__ == '__main__':
  app.run_server(debug=True, port=8080)
