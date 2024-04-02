from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd




edad_part = ('Entre 16 y 18 años', 'Entre 24 y 35 años', 'entre 35 y 45 años', 
          'Entre 45 y 55 años', '+ 60 años')

cant_part= [21, 37, 30, 15, 3]

df= pd.DataFrame({"Edad":edad_part, "Número de participantes":cant_part})

app_dash = Dash(__name__)

fig = px.bar(df, x=df['Edad'], y=df['Número de participantes'], color='Edad')

fig.update_layout(plot_bgcolor='#999999',
                  paper_bgcolor='#999999',
                  font_color='#222222'
                 )

app_dash.layout= html.Div(children=[
                          html.H1(children='Estudio económico en Sarmiento', style={'textAlign':'center'}),

                          html.P(children='hola mundo quiero trabajar por favor'),

                          html.Div(children='''Plotly'''),

                          dcc.Graph(id='example-graph',
                                    figure=fig
                                    )
                         ])


def update_graph():
    return px.bar(x=df['Edad'], y=df['Profesión'])




if __name__ == '__main__':
    app_dash.run(debug=True)