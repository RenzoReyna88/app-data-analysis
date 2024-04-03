from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd




edad_part = ('Entre 16 y 18 años', 'Entre 24 y 35 años', 'entre 35 y 45 años', 
          'Entre 45 y 55 años', '+ 60 años')

cant_part= [21, 37, 30, 15, 3]

df= pd.DataFrame({"Rango de edades":edad_part, "Número de participantes":cant_part})

app = Dash(__name__)

server= app.server


colors_bar= ['#001F49', '#CB0000', '#006B37', '#5200F4', '#FF6100']




fig = px.bar(df, x=df['Rango de edades'], y=df['Número de participantes'], color='Rango de edades')


app.layout= html.Div(children=[
                               html.H1(children='Estudio económico en Sarmiento (Informe final)', style={'textAlign':'center'}),

                               html.P(children='Aquí el Resumen de todo la investigación', 
                                      style={'textAlign':'center'}),

                                html.Br(),

                                dcc.Graph(id='example-graph',
                                        figure=fig
                                       )
                              ]
                    )

fig.update_layout(title=dict(text='Número de participantes según su edad'),
                  legend=dict(y=0.9,x=1.0, bgcolor="white"),
                  plot_bgcolor='#d9d9d9',
                  paper_bgcolor='#d9d9d9',
                  font_color='#333333'
                 )




if __name__ == '__main__':
    app.run(debug=True)