# import dash
# import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
from flask import Flask
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# flask_server = Flask(__name__)
# app = dash.Dash(__name__, server=flask_server, external_stylesheets=[dbc.themes.BOOTSTRAP])
# server = app.server
app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])


@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, port="8000")


# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


# if __name__ == '__main__':
#     app.run()
