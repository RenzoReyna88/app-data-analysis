from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



# Inicialización de la app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server= app.server

# Lectura de archivos CSV
edades_participantes= pd.read_csv("datos/edades_participantes.csv", sep=',')

prob_de_vivir_sarm= pd.read_csv("datos/prob_de_vivir_sarm.csv", sep=',')

resp_sueldo= pd.read_csv("datos/sueldo.csv", sep=',')

df_int_soc= pd.read_csv("datos/df_int_soc.csv", sep=',')

ddf= pd.read_csv("datos_encuestados.csv", sep=',')
ddff= ddf.head(6)


# Iniciar ploteo de figuras
# Figura n° 1 gráfico de barras
fig_edades = px.bar(edades_participantes, x=edades_participantes['Rango de edades'], y=edades_participantes['Número de participantes'], 
                    color='Rango de edades'
                    )
fig_edades.update_layout(title=dict(text='Números de participantes según su edad'),
                                    plot_bgcolor='lightslategrey',
                                    paper_bgcolor='lightslategrey',
                                    font_color='white',
                        )

# Figura n° 2 gráfico de barras
fig_num_part = px.bar(resp_sueldo, x=resp_sueldo['Porcentajes respuestas'], y=resp_sueldo['Respuesta sobre el sueldo'], 
                                     color='Porcentajes respuestas'
                      )
fig_num_part.update_layout(title=dict(text='Promedio ingresos mensuales'),
                                      plot_bgcolor='lightslategrey',
                                      paper_bgcolor='lightslategrey',
                                      font_color='white'
                            )

# Figura n° 3 gráfico circular
fig_int_soc = go.Figure(data=[go.Pie(labels=df_int_soc['Intención social'], values=df_int_soc['Respuestas'], hole=.3,
                                     pull=[0, 0, 0, 0, 0, 0.09])
                              ]
                        )
fig_int_soc.update_layout(title_text="Intención social cómo representante público", 
                          uniformtext_minsize=9, 
                          uniformtext_mode='hide',
                          legend=dict(
                                      x=0.9,  
                                      y=1.2,  
                                      orientation='h'
                                     )
                          )

# Figura n° 4 gráfico de dispersión
fig_estudios = px.scatter(ddf, x=ddf['Nivel de estudios'], y=ddf['Profesión'], color='Nivel de estudios',
                          )
fig_estudios.update_layout(title=dict(text='Profesión vs Estudios'),
                                      plot_bgcolor='lightslategrey',
                                      paper_bgcolor='lightslategrey',
                                      font_color='white',
                                      font_size=10,
                            legend=dict(
                                        x=1.0,  
                                        y=1.2, 
                                        orientation='v' 
                                    ),
                            yaxis_title_font=dict(size=12),
                            xaxis_title_font=dict(size=12)
                            )

# Diseño de la aplicación (Interfaz)
app.layout= dbc.Container([
                           dbc.Row([    
                                    dbc.Col(children=[ 
                                                       html.Br(),

                                                       html.H1(children=['Estudio económico en Sarmiento (Informe final)'],                                         
                                                               style={'textAlign':'left'}),
                                                       html.Hr(),            
                                
                                                       html.P(children=["""Este informe resume los hallazgos del estudio económico realizado en la localidad de Sarmiento, pueblo ubicado en el departamento Totoral, 
                                                                        provincia de Córdoba. En esta investigación se analizaron las respuestas a 15 preguntas de opción múltiple choise. 
                                                                        En el estudio participaron 105 personas aportando una mirada critica sobre las condiciones socioeconómica en la localidad. Es impportante tener en cuenta
                                                                        qué esta investigación permite evaluar las condiciones de la población, y más importante aun, permite identificar las necesidades de cada sector o área y 
                                                                        mejorar la toma de decisiones, el desarrollo y la innovación de esta hermosa Localidad."""],                                      
                                                                        style={'textAlign':'left'}),

                                                       html.Br(),

                                                       dash_table.DataTable(data=ddff.to_dict('records'), style_table={'overflowX': 'auto'}),

                                                       html.Br()

                                    ]),

                                    dbc.Col([
                                            html.H5(children='Analizando algunas variables:'),
                                            html.Ul(children=[
                                                            html.Ol(children=[
                                                                            '''1. la edad de Los participantes se concentró entre 24 y 45 años (67%). 
                                                                    Los menores de 24 años y mayores de 60 años son los grupos menor participación (24%).'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''2. En cuánto a profesión Predominó el trabajo independiente (38%). Le siguen "Empleado" (27%) 
                                                                    y "Desempleado" (21%).'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''3. El Nivel de estudios más común es "Primario Secundario" (42%).
                                                                    Le siguen "Primario" (35%) y "Universitario" (18%).'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''4. El ingreso mensual se concentra entre $10.000 y $30.000 (45%).
                                                                    El (43%) gana menos de $30.000.'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''5. Capacidad de ahorro: El (38%) no puede ahorrar.
                                                                    El (62%) ahorra menos del (25%) de su ingreso.'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''6. "Mejorar el sistema educativo" es la principal intención social de los participantes (42%).
                                                                    Le sigue "Generar trabajo" (35%).'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''7. La atención médica local y la falta de ampliación de servicios son las principales críticas (42%).
                                                                    El (54%) califica los servicios del comercio local como "Excelentes".'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''8. El (62%) considera las fuentes de trabajo local como "Muy necesarias".
                                                                    El (79%) cree que el trabajo de la cooperativa es "Muy eficiente" o "Eficiente".'''
                                                            ]),
                                                            html.Ol(children=[
                                                                            '''9. El (78%) considera "Muy probable" seguir viviendo en Sarmiento aun sin contar con mayores
                                                                    recursos que garanticen el crecimeinto.'''                                                                                          
                                                            ]),

                                            ]),

                                                            
                                    ]),                                
                          ]),                            

                            html.Br(),

                          dbc.Row([
                                   dbc.Col([
                                            html.H3(children=['¡Vamos a los Gráficos!'],                                         
                                                                   style={'textAlign':'left'}),

                                            html.Br(),

                                            dcc.Graph(id='rango_edades-graph', figure=fig_edades),                    
                                            html.Hr(),
                                            dcc.Graph(id='ingreso_mensual-graph', figure=fig_num_part),
                                   ])
                          ]),

                             html.Br(),

                          dbc.Row([
                                   dbc.Col([
                                            dcc.Graph(id='int_social-graph', figure=fig_int_soc),
                                   ], width=12),
                                
                          ]),

                            html.Br(),

                          dbc.Row([
                                   dbc.Col([
                                            dcc.Graph(id='profesion_niv_estudios-graph', figure=fig_estudios)
                                   ], width=12),                       
                          ]),
                            
                            html.Br(),

                          dbc.Row([
                                   dbc.Col([
                                            html.H5('Conclusiones finales:'),
                                                                    
                                            html.P(children=['''Entre los participantes del estudio, una población joven y dinámica se enfrenta a desafíos y oportunidades. 
                                                    Su nivel educativo, aunque moderado, refleja un deseo de crecimiento y superación. Sin embargo, la realidad económica no 
                                                    siempre acompaña estas aspiraciones. El tejido laboral es diverso. Muchos se dedican al trabajo independiente, pero también 
                                                    existe un porcentaje significativo de desempleo. Los ingresos mensuales son bajos para la mayoría, lo que limita la capacidad 
                                                    de ahorro y la calidad de vida.'''
                                                                                    
                                            ]),

                                            html.P(children=['''Los encuestados valoran la educación y la generación de empleo como prioridades clave. A pesar de los desafíos, existe una percepción positiva,
                                                    las fuentes de trabajo son apreciadas, y la mayoría de los habitantes desean permanecer en Sarmiento.
                                                    Sin embargo, no todo es perfecto. La atención médica local necesita mejoras, y la juventud busca oportunidades para crecer y prosperar. 
                                                    En este equilibrio entre desafíos y esperanzas, se mantiene una mirada optimista hacia el futuro.'''
                                            ]),
                                   ])
                          ]),

                            html.Br(),

                            html.Hr(),

                           dbc.Row([
                                    dbc.Col([
                                             html.Br(),
                                             html.Img(src=app.get_asset_url('Desarrolllador-Sarmientino.jpg'), 
                                                               style={'height': '200px', 'width': 'auto', 'display': 'block', 'margin': '0 auto'}),
                                             html.P(children=['Data analyst / Python developer'], 
                                                               style={'font-weight': 'bold', 'textAlign':'center'})
                                    ], width=5),

                                    dbc.Col([
                                             html.Div([
                                                       html.P(children=['''Mi nombre es Renzo Reyna. Soy un autodidacta con un fervoroso deseo hacia el conocimiento 
                                                                        tecnológico y la ciencia de datos.'''
                                                       ], style={'font-weight': 'bold', 'margin-top': '20px', 'textAlign':'start'}),
                                                       html.P(children=['''Llevo 6 años estudiando economia, comportamiento de mercado e inserción de la tecnología en 
                                                                    el ámbito social. En Los ultimos 2 años incursione en el mundo de la programación Python y el 
                                                                    analisis de datos. Desde entonces, me he dedicado a comprender en profundidad estas tecnologías 
                                                                    y a cómo aplicarlas a nuestras activades con el fin de mejorar nuestro ambiente de Trabajo
                                                                    y cada proceso que llevemos adelante en la vida a diario.'''])    
                                                                                                                                                  
                                             ])                                                    
                                    ], width=6),

                                    dbc.Col([], width=1)

                           ]),

                           html.Br(),


            ])


# Ejecución solo si el módulo o variable nombrado/a "app" es el módulo principal del programa.
if __name__ == '__main__':
    app.run_server(debug=True)
