import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.DataFrame({
    'studente_id' : range()
})

all_options = {
    'Brasil': ['Rio de Janeiro', 'Minas Gerais', 'Paraná'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(
        id='countries-radio',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='Brasil'
    ),

    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values')
])

# Retorna as cidade por país
@app.callback(
    Output('cities-radio', 'options'), # vira input no callback de cidades
    [Input('countries-radio', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

# Retorna as cidades
@app.callback(
    Output('cities-radio', 'value'),
    [Input('cities-radio', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

# Retorna a opcão/detalhes da cidade
@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
     Input('cities-radio', 'value')])
def set_display_children(selected_country, selected_city):
    return u'{} é uma cidade do {}'.format(
        selected_city, selected_country,
    )


if __name__ == '__main__':
    app.run_server(debug=True)