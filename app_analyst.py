from dash import Dash, html, dcc, callback, Output, Input, State
import dash_leaflet as dl

import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd



# Inicialización de la app
app= Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server= app.server


PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

# Lectura de archivos CSV
edades_participantes= pd.read_csv("datos/edades_participantes.csv", sep=',')

prob_de_vivir_sarm= pd.read_csv("datos/prob_de_vivir_sarm.csv", sep=',')

resp_sueldo= pd.read_csv("datos/sueldo.csv", sep=',')

df_int_soc= pd.read_csv("datos/df_int_soc.csv", sep=',')

corr_respuestas= pd.read_csv("datos/var_corr.csv", sep=',')

ddf= pd.read_csv("datos/datos_encuestados.csv", sep=',')
ddff= ddf.head(6)


# Iniciar ploteo de figuras

# Figura n° 1 gráfico de barras

fig_edades = px.bar(edades_participantes, x=edades_participantes['Rango de edades'], y=edades_participantes['Participación'], 
                    color='Participación', text_auto= True
                    )
fig_edades.update_layout(title=dict(text='Participantes según su edad', y=0.92),
                         plot_bgcolor='#0C2547',
                         paper_bgcolor='#0C2547',
                         font_color='white',

                         legend=dict(font_size=9),
                         yaxis_tickfont=dict(size=9),
                         xaxis_tickfont=dict(size=9)                         
                        )

# Figura n° 2 gráfico de barras

fig_sueldo_aprox = px.bar(resp_sueldo, x=resp_sueldo['Respuestas'], y=resp_sueldo['Respuesta sobre el sueldo'], 
                          color='Respuestas', text_auto=True
                         )

fig_sueldo_aprox.update_traces(texttemplate='%{x:.0f}%')


fig_sueldo_aprox.update_layout(title=dict(text='Promedio ingresos mensuales', y=0.92),
                               plot_bgcolor='#0C2547',
                               paper_bgcolor='#0C2547',
                               font_color='white',
                               font_size=12,
                               legend=dict(
                                          font_size=6,
                                          y= 0.72),
                               yaxis_tickfont=dict(size=9),
                               xaxis_tickfont=dict(size=9)                                          
                              )

# Figura n° 3 gráfico circular

fig_int_soc = go.Figure(data=[go.Pie(labels=df_int_soc['Intención social'], values=df_int_soc['Respuestas'], hole=.2,
                                     pull=[0, 0, 0, 0, 0, 0.09], textinfo='percent', rotation=-60, marker=dict(colors=['#FEBFB3', '#E1396C', '#96D38C', '#D0F9B1']))
                              ]
                        )
fig_int_soc.update_layout(title_text="Intención social cómo representante público", 
                          uniformtext_minsize=9, 
                          uniformtext_mode='hide',
                          paper_bgcolor= '#0C2547',
                          font_color='white',
                          font_size=12,

                          legend=dict(
                                      title=('Respuestas'),
                                      x=0.95,  
                                      y=1.1,  
                                      orientation='v',
                                      font_size=6
                          ),
                          )


# Figura n° 4 gráfico de dispersión
fig_estudios = px.scatter(ddf, x=ddf['Nivel de estudios'], y=ddf['Profesión'], color='Nivel de estudios',
                           size=[1]*len(ddf)
                          )
fig_estudios.update_layout(title=dict(text='Profesión vs nivel de Estudios', y=0.92),
                           plot_bgcolor='#0C2547',
                           paper_bgcolor='#0C2547',
                           font_color='white',
                           font_size=12,

                           legend=dict(
                                       x=1.1,  
                                       y=0.72, 
                                       orientation='v',
                                       font_size=6
                           ),

                            yaxis_tickfont=dict(size=9),
                            xaxis_tickfont=dict(size=9)
                           )

# Figura n° 5 Mapa de calor

fig_corr_variables= px.imshow(corr_respuestas.corr(), color_continuous_scale='RdBu'
                              )

fig_corr_variables.update_layout(title=dict(text='Correlación entre las respuestas analizadas', y=0.92),
                                 xaxis_title= 'Eje x',
                                 yaxis_title= 'Eje y',
                                 font=dict(size=12, color='white'),
                                 yaxis_tickfont=dict(size=8.1, color='white'),
                                 xaxis_tickfont=dict(size=8.1, color='white'),
                                 paper_bgcolor= '#0C2547'
                                )


# Diseño de la aplicación (Interfaz)
app.layout= dbc.Container([    
                           dbc.Navbar(
                                    dbc.Container([
                                                    html.A(
                                                        # Use row and col to control vertical alignment of logo / brand
                                                            dbc.Row([
                                                                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                                                                    dbc.Col(dbc.NavbarBrand("desarrolladorsarmientino.com", className="ms-3", style={'color':'white'})),
                                                            ],
                                                            align="center",
                                                            className="g-0",
                                                            ),
                                                            href="https://www.desarrolladorsarmientino.com/",
                                                            style={"textDecoration": "none"}
                                                    ),
                                                    dbc.Nav([
                                                            dbc.NavItem(dbc.NavLink(html.Img(src='/assets/FACEBOOK_icon.png', width="18px", height="18px"), href="https://www.facebook.com/desarrollador.sarmientino")),
                                                            dbc.NavItem(dbc.NavLink(html.Img(src='/assets/SUBSTACK_icon.png', width="18px", height="18px"), href="https://substack.com/@renzoreynahttps://substack.com/@renzoreyna")),
                                                            dbc.NavItem(dbc.NavLink(html.Img(src='/assets/INSTAGRAM_icon.png', width="18px", height="18px"), href="https://www.instagram.com/desarrollador.sarmientino/?hl=es")),
                                                            dbc.NavItem(dbc.NavLink(html.Img(src='assets/LINKEDIN_icon.png', width="18px", height="18px"), href="https://www.linkedin.com/in/renzo-reyna/")),
                                                            dbc.NavItem(dbc.NavLink(html.Img(src='assets/GITHUB_icon.png', width="18px", height="18px"), href="https://github.com/RenzoReyna88")),
                                                            
                                                    ], className="ms-auto") 
                                                    
                                    ]),
                                    color="#0C2547",
                           ),  
                           
                          html.Br(),
                                
                          dbc.Row([    
                                  html.H1(children=['Estudio económico en Sarmiento: Análisis general sobre sus condiciones sociales'],                                         
                                                    style={'textAlign':'left', 'color':'#0C2547'}),
                                  html.Hr(),                                     


                                  html.P(children=["""Este informe resume los hallazgos del estudio económico realizado en la localidad de Sarmiento, pueblo ubicado en el departamento 
                                                   Totoral, provincia de Córdoba."""],                                      
                                                  style={'textAlign':'left'}),

                                  dbc.Col([], lg=3, md=3),

                                  dbc.Col(className="d-flex justify-content-center", children=[ 
                                                  dl.Map(center=[-30.77263581688577, -64.11194991190187], style={'width':'600px', 'height':'300px', 'textAlign':'center',  'border': '3px'}, zoom=13, children=[
                                                            dl.TileLayer(id="base-layer-id"),
                                                            dl.Marker(position=[-30.77263581688577, -64.11194991190187], children=[
                                                                                                                                  dl.Tooltip('Localidad de Sarmiento'),
                                                                                                                                  dl.Popup([
                                                                                                                                           html.H1("Localidad de Sarmiento, Totoral , Córdoba, Argentina"),
                                                                                                                                           html.P('Latitud: -30.77263581688577, Longitud: -64.11194991190187')
                                                                                                                                  ])
                                                            ]),

                                                            dl.LayersControl(
                                                                            [dl.BaseLayer(dl.TileLayer(url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"), name='Mapa de Calles'),
                                                                            dl.BaseLayer(dl.TileLayer(url="https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png"), name='Mapa en Blanco y Negro'),
                                                                            dl.BaseLayer(dl.TileLayer(url="https://tiles.wmflabs.org/hikebike/{z}/{x}/{y}.png"), name='Mapa de Ciclismo'),
                                                                            dl.BaseLayer(dl.TileLayer(url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"), name='Imágenes Satelitales')]
                                                            )
                                                   ]),

                                                                                                     
                                  ], lg=6, md=6),

                                  dbc.Col([], lg=3, md=3),
                                  html.Div(children=[html.P('''* Sarmiento es un pueblo ubicando al norte de la provincia de Córdoba. 
                                                            Su población ronda los 1.250 hab. Aproximadamente.''')
                                  ], style={'fontSize':'9px','textAlign':'center', 'marginTop':'18px',}),


                                  html.Br(),

                                  html.P(children=["""En la investigación se analizaron las respuestas a 15 preguntas de opción múltiple choise. En el estudio participaron 105 personas 
                                                   aportando una mirada critica sobre las condiciones socioeconómica en la localidad. Es importante comprender, qué este tipo de investigación permite 
                                                   evaluar las condiciones de la población e identificar las necesidades de cada sector o área. Con lo cuál, esto permite abordar los problemas con mayor
                                                   precisión, optimizar la asignación de los recursos, mejorar la toma de decisiones y contribuír al desarrollo y la innovación."""],                                      
                                         style={'textAlign':'left'}),
                          ]),

                          html.Br(),

                          dbc.Row([
                                  html.H4(children=['¡Vamos a los Gráficos!'],                                         
                                                style={'textAlign':'center', 'color':'#0C2547'}),

                                  dbc.Col([
                                  ], lg=1, md=1),               
                                 
                                  dbc.Col([
                                          dcc.Graph(id='rango_edades-graph', figure=fig_edades), 
                                          html.P(children=['''*En la imagen anterior se puede observar que la edad de Los participantes se concentró entre los 24 y 45 años. 
                                                           Los participantes entre 45 y 55 años, junto a los mayores de 60 años. Son los grupo de menor participación.'''], 
                                                        style={'fontSize':'12px'})                   
                                  ], lg=10, md=10),

                                  dbc.Col([
                                  ], lg=1, md=1)
                          ]),     

                          html.Br(),

                          dbc.Row([
                                  dbc.Col([
                                  ], lg=1, md=1),

                                  dbc.Col([
                                          dcc.Graph(id='sueldo_aprox-graph', figure=fig_sueldo_aprox),   
                                          html.P(children=['''* El gráfico anterior ilustra la distribución del salario de los participantes. Se observa que la mayoría de los ingresos mensuales 
                                                           se concentran entre $30.000 y $400.000, representando al (54%) de los participantes. Por otro lado, un (12%) de los participantes 
                                                           gana entre $10.000 y $30.000, Y un (35%) no reporta ingresos mensuales.'''], 
                                                        style={'fontSize':'12px'})                                    
                                  ], lg=10, md=10),

                                  dbc.Col([
                                  ], lg=1, md=1),
                          ]),

                          html.Br(),

                          dbc.Row([   
                                  dbc.Col([
                                  ], lg=1, md=1),

                                  dbc.Col([
                                          dcc.Graph(id='int_social-graph', figure=fig_int_soc),
                                          html.P(children=['''* El gráfico presentado ilustra las respuestas a la pregunta: ‘Si fueras un representante público, ¿qué acción tomarías?’. 
                                                           Se observa una tendencia marcada hacia la opción ‘Haría todo lo anterior’, que engloba todas las alternativas excepto 
                                                           Dejaría todo como está’. Esta última opción fue seleccionada por un solo participante.'''], 
                                                    style={'fontSize':'12px'}) 
                                  ], lg=10, md=10),

                                  dbc.Col([
                                  ], lg=1, md=1)
                          ]),      

                          html.Br(),

                          dbc.Row([
                                  dbc.Col([
                                      ], lg=1, md=1),

                                  dbc.Col([
                                          html.H3(children='Analizando variables de la investigación:', style={'color':'#0C2547'}),
                                          html.Ul(children=[
                                                           html.Ol(children=[
                                                                           '''1. la edad de Los participantes se concentró entre 24 y 45 años (67%). 
                                                                   Los menores de 24 años y mayores de 60 años son los grupos de menor participación (24%).'''
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
                                                                           '''4. El ingreso mensual se concentra entre $30.000 y $400.000 (54%).
                                                                   Mientras que el (12%) gana entre $12.000 y $30.000.'''
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
                                                                   recursos que garanticen el crecimiento.'''                                                                                          
                                                           ])
                                          ]),
                                  ], lg=10, md=9),

                                  dbc.Col([
                                  ], lg=1, md=1),
                          ]),

                          html.Br(),

                          dbc.Row([
                                  dbc.Col([
                                  ], lg=1, md=1),

                                  dbc.Col([
                                          dcc.Graph(id='profesion_niv_estudios-graph', figure=fig_estudios),
                                          html.P(children=['''* El gráfico anterior muestra la distribución de las variables ‘Profesión vs Nivel de Estudio’. 
                                                           Se puede observar un patrón en el que la mayoría de las actividades laborales están ocupadas por 
                                                           personas que han completado sus estudios primarios y secundarios. Esta información proporciona una comprensión sólida de 
                                                           cómo la educación y la profesión están interrelacionadas, además de la importancia de la educación para el desempeño profesional.'''], 
                                                        style={'fontSize':'12px'}) 
                                  ], lg=10, md=10),

                                  dbc.Col([
                                  ], lg=1, md=1)   

                          ]),

                          html.Br(),

                          dbc.Row([
                                  dbc.Col([
                                  ], lg=1, md=1),

                                   dbc.Col([
                                           dcc.Graph(id='corr_variables-graph', figure=fig_corr_variables),
                                           html.P(children=['''* El mapa de calor presentado anteriormente ilustra la correlación entre los valores asociados a las respuestas de cada 
                                                               pregunta formulada en el estudio económico. Un color más intenso denota una correlación más fuerte, mientras que una disminución 
                                                               en la intensidad del color sugiere una ausencia de relación entre las variables en cuestión. Este patrón de colores facilita la 
                                                               interpretación de las interacciones entre las variables estudiadas.'''], style={'fontSize':'12px'})                                           
                                   ], lg=10, md=10),

                                   dbc.Col([
                                   ], lg=1, md=1)     
                          ]),
                            
                          html.Br(),

                          dbc.Row([
                                  dbc.Col([], lg=2, md=1),

                                  dbc.Col([
                                          html.Img(src='assets/nube_estudio_economico.png', width="400px", height="300px")
                                  ], lg=8, md=8),

                                  dbc.Col([], lg=2, md=1)

                          ]),

                          html.Br(),

                          dbc.Row([
                                  dbc.Col([], lg=1, md=1),

                                  dbc.Col([
                                            html.H5('Conclusiones finales:', style={'color':'#0C2547'}),
                                                                    
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
                                  ], lg=10, md=10),

                                  dbc.Col([], lg=1, md=1)
                          ]),

                          html.Br(),

                          html.Hr(),

                          dbc.Row([
                                  dbc.Col([
                                          html.Br(),
                                          html.Img(src=app.get_asset_url('Desarrolllador-Sarmientino.jpg'), 
                                                    style={'height': '170px', 'width': 'auto', 'borderRadius':'9px', 'display': 'block', 'margin': '0 auto'}),

                                          html.P(children=['Data analyst / Python developer'], 
                                                    style={'font-weight': 'bold', 'textAlign':'center', 'fontSize': '9px'})
                                  ], lg=4, md=4),

                                  dbc.Col([
                                          html.Div([
                                                   html.P(children=['''Mi nombre es Renzo. Soy nativo de una pequeña localidad al norte de la Provincia de Córdoba llamada Sarmiento. Me considero 
                                                                    un autodidacta y entusista por el conocimiento tecnológico y la ciencia de datos.''']),

                                                   html.P(children=['''Hace seis años, emprendí un camino de autoaprendizaje en economía, comportamiento de los mercados e integración 
                                                                    de la tecnología en el ámbito social. Durante el último año y medio, me adentré en el mundo de la programación 
                                                                    Python y el Análisis de Datos. Desde entonces, he fusionado mis conocimientos y habilidades adquiridas durante 
                                                                    este tiempo, dedicándome a comprender en profundidad cómo estas tecnologías pueden generar beneficios económicos 
                                                                    y sociales al aplicarlas a nuestras actividades, con el objetivo de mejorar nuestro entorno laboral y 
                                                                    cada proceso que llevamos a cabo a partir de la toma de decisiones.''']),

                                                   html.H6(children=["¡", html.A('Trabajemos Juntos', href='https://www.desarrolladorsarmientino.com/perfil', style={'textDecoration':'none', 'font-weight': 'bold', 'color':'#0C2547'}),"!"])                                                                                                                
                                          ], style={'font-weight': 'bold', 'margin-top': '20px', 'textAlign':'start', 'fontSize':'14px'}),
                                  ], lg=8, md=8)
                          ]),

                          html.Br(),

                          dbc.Row([
                                dbc.Col([], lg=4, md=4),
                                  dbc.Col([
                                          html.Div([
                                                   dbc.Button("Contacto", id="collapse-button", className="mb-3", n_clicks=0, style={'backgroundColor':'#0C2547'}),
                                          ]),
                                          html.Div([
                                                   dbc.Collapse(
                                                               dbc.Card(children=[
                                                                                 dbc.CardHeader(html.H6("Información personal:"), style={"backgroundColor":"#0C2547", "color":"white"}),
                                                                                 dbc.CardBody(children=[
                                                                                                       html.P("TEL: +54 3525-620842", className="Card-cel"),
                                                                                                       html.P("desarrollador.sarmientino@gmail.com", className="mail-one"),
                                                                                                       html.P("DS.techsolutions@outlook.com", className="mail-two"),
                                                                                                       html.P("Independencia s/n - Sarmiento, Córdoba, Argentina.", className="direc"),
                                                                                                       html.A('www.desarrolladorsarmientino.com', href='https://www.desarrolladorsarmientino.com/perfil')
                                                                                 ], style= {"fontSize":"15px"})

                                                               ], style={"width":"300px"}),id="horizontal-collapse",
                                                                   is_open=False,
                                                                   dimension="width"
                                                   )
                                      ], style={"minHeight": "90px"})  
                                  ], lg=8, md=8),

                          ]),

                          html.Footer(                                     
                                     html.Div([
                                              html.Div(className="d-flex justify-content-center", children=[
                                                                                                           html.Div(className="col-sm-4"),

                                                                                                           html.Div(className="col-sm-4", 
                                                                                                                    children=[
                                                                                                                             html.P("Redes sociales:", className="text-center", 
                                                                                                                                     style={"font-family": "'Lato', sans-serif;"}),
                                                                                                                             html.Div(className="d-flex justify-content-center", children=[
                                                                                                                                                                                          html.Div(className="col-sm-1 text-center me-3", children=[
                                                                                                                                                                                                                                                   html.A(href="https://www.facebook.com/renzoreyna.88/", target="_blank", 
                                                                                                                                                                                                                                                          rel="noopener noreferrer", children=[
                                                                                                                                                                                                                                                                                              html.Img(src="assets/facebook-logo.png", width="24", 
                                                                                                                                                                                                                                                                                              height="24")
                                                                                                                                                                                                                                                   ])
                                                                                                                                                                                           ]),

                                                                                                                                                                                           html.Div(className="col-sm-1 text-center me-3", children=[
                                                                                                                                                                                                                                                    html.A(href="https://substack.com/@renzoreyna", target="_blank", 
                                                                                                                                                                                                                                                           rel="noopener noreferrer", children=[
                                                                                                                                                                                                                                                                                               html.Img(src="assets/substack-logo.png", width="24", 
                                                                                                                                                                                                                                                                                               height="21", 
                                                                                                                                                                                                                                                                                               style={"text-decoration": "none", "color": "rgb(196, 79, 16)"})
                                                                                                                                                                                                                                                    ])
                                                                                                                                                                                           ]),

                                                                                                                                                                                           html.Div(className="col-sm-1 text-center me-3", children=[
                                                                                                                                                                                                                                                    html.A(href="https://github.com/RenzoReyna88", target="_blank", 
                                                                                                                                                                                                                                                           rel="noopener noreferrer", children=[
                                                                                                                                                                                                                                                                                               html.Img(src="assets/github-logo.png", width="24", 
                                                                                                                                                                                                                                                                                               height="24", 
                                                                                                                                                                                                                                                                                               style={"text-decoration": "none", "color": "rgb(0, 0, 0)"})
                                                                                                                                                                                                                                                    ])
                                                                                                                                                                                           ]),

                                                                                                                                                                                           html.Div(className="col-sm-1 text-center me-3", children=[
                                                                                                                                                                                                                                                    html.A(href="https://www.instagram.com/reynarenzo88/", target="_blank", 
                                                                                                                                                                                                                                                           rel="noopener noreferrer", children=[
                                                                                                                                                                                                                                                                                               html.Img(src="assets/instagram-logo.png", width="24", 
                                                                                                                                                                                                                                                                                               height="24", 
                                                                                                                                                                                                                                                                                               style={"text-decoration": "none", "color": "rgb(196, 16, 22)"})
                                                                                                                                                                                                                                                    ])
                                                                                                                                                                                           ]),

                                                                                                                                                                                           html.Div(className="col-sm-1 text-center me-3", children=[
                                                                                                                                                                                                                                                    html.A(href="https://twitter.com/Reynarenzo88", target="_blank", 
                                                                                                                                                                                                                                                           rel="noopener noreferrer", children=[
                                                                                                                                                                                                                                                                                               html.Img(src="assets/twitter-logo.png", width="30", 
                                                                                                                                                                                                                                                                                               height="24", 
                                                                                                                                                                                                                                                                                               style={"text-decoration": "none", "color": "rgb(39, 39, 39)"})
                                                                                                                                                                                                                                                    ])
                                                                                                                                                                                           ]),

                                                                                                                                                                                           html.Div(className="col-sm-1 text-center me-3", children=[
                                                                                                                                                                                                                                                    html.A(href="https://www.linkedin.com/in/renzo-reyna/", target="_blank", 
                                                                                                                                                                                                                                                           rel="noopener noreferrer", children=[
                                                                                                                                                                                                                                                                                               html.Img(src="assets/linkedin-logo.png", width="24", 
                                                                                                                                                                                                                                                                                               height="24")
                                                                                                                                                                                                                                                    ])
                                                                                                                                                                                           ]),
                                                                                                                             ]),
                                                                                                           ]),

                                                                                                           html.Div(className="col-sm-4"),
                                               ]),

                                     html.Br(),          

                                     html.P(children=['© Todos los derechos reservados - ', html.A('desarrolladorsarmientino.com', href='https://www.desarrolladorsarmientino.com', style={'textDecoration':'none', 'font-weight': 'bold', 'color':'#0C2547'}), ' 2023 - 2024.']),

                                     ], style={'textAlign': 'center', 'padding': '18px', 'color':'black', 
                                               'fontSize':'15px'},

                                     )
                          ),

                          html.Br(),
                          html.Br(),
                          html.Br()                            
            ])

@app.callback(
    Output("horizontal-collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("horizontal-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# Ejecución solo si el módulo o variable nombrado/a "app" es el módulo principal del programa.
if __name__ == '__main__':
    app.run_server(debug=True)
