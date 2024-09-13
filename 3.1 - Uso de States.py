import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-1", type="text", value="Montreal"),
    dcc.Input(id="input-2", type="text", value="Canada"),
    html.Button(id="submit-button-state", children='Submit'),
    html.Div(id="number-output"),
])

@app.callback(
    Output("number-output", "children"),
    Input('submit-button-state', 'n_clicks'),  # Correção: 'n_clicks' em vez de 'n-clicks'
    State("input-1", "value"),
    State("input-2", "value")
)
def update_output(n_clicks, input1, input2):  # Adicionar 'n_clicks' como primeiro parâmetro
    return u'Input 1 is "{}" and Input 2 is "{}"'.format(input1, input2)

if __name__ == '__main__':
    app.run_server(debug=True)
