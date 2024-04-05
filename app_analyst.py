from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate



# Inicialización de la app Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server= app.server

# Lectura de archivos CSV
edades_participantes= pd.read_csv("datos/edades_participantes.csv", sep=',')

prob_de_vivir_sarm= pd.read_csv("datos/prob_de_vivir_sarm.csv", sep=',')

resp_sueldo= pd.read_csv("datos/sueldo.csv", sep=',')

ddf= pd.read_csv("datos_encuestados.csv", sep=',')
ddff= ddf.head(11)

# Ploteo de las figuras
# Figura n° 1
fig_edades = px.bar(edades_participantes, x=edades_participantes['Rango de edades'], y=edades_participantes['Número de participantes'], 
                    color='Rango de edades')
fig_edades.update_layout(title=dict(
                                        text='Números de participantes según su edad'),
                                        plot_bgcolor='lightslategrey',
                                        paper_bgcolor='lightslategrey',
                                        font_color='white'
                            )

# Figura n° 2
fig_num_part = px.bar(resp_sueldo, x=resp_sueldo['Porcentajes respuestas'], y=resp_sueldo['Respuesta sobre el sueldo'], 
                      color='Respuesta sobre el sueldo')
fig_num_part.update_layout(title=dict(
                                        text='Salario promedio'),
                                        plot_bgcolor='lightslategrey',
                                        paper_bgcolor='lightslategrey',
                                        font_color='white'
                            )

# Figura n° 3
fig_estudios = px.scatter(ddf, x=ddf['Nivel de estudios'], y=ddf['Profesión'], color='Nivel de estudios')
fig_estudios.update_layout(title=dict(
                                        text='Profesión frente a nivel de estudios'),
                                        plot_bgcolor='lightslategrey',
                                        paper_bgcolor='lightslategrey',
                                        font_color='white',
                            )

# Diseño de la aplicación (Interfaz)
app.layout = dbc.Container([

                            dbc.Row([
                                    html.Div(children=[
                                                        html.H3(children='Estudio económico en Sarmiento (Informe final)', 
                                                                style={'textAlign':'center'}),
                                                        html.P(children='Aquí el Resumen de todo la investigación', 
                                                               style={'textAlign':'center'}),

                                                        html.Br(),
                                                        
                                                        dcc.Graph(id='edades-graph', figure=fig_edades),
                                            ])
                            
                            ]),

                            html.Br(),

                            dbc.Row([
                                    dbc.Col([
                                            html.Div(children=[html.H3(children=['Respuestas de los participantes'])
                                                               ]),
                                
                                            dash_table.DataTable(data=ddff.to_dict('records'), style_table={'overflowX': 'auto'}),
                                    ],width=4),

                                    dbc.Col([
                                            dcc.Graph(id='estudios-graph', figure=fig_num_part),
                                    ], width=8)
                            ]),

                            dbc.Row([
                                    dbc.Col([
                                        html.Div(children=[
                                            html.H3(children='texto', style={'textAlign':'center'}),
                                            html.P(children='texto', style={'textAlign':'center'}),
                                            html.Br(),
                                            dcc.Graph(id='profesion-graph', figure=fig_estudios)
                                            ])
                                    ])
                            
                            ]),

            ])

# Ejecución del programa, solo si el módulo o variable nombrada "app" es el módulo principal.
if __name__ == '__main__':
    app.run_server(debug=True)
