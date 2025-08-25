from dash import Dash, html, dcc

import plotly.express as px

app = Dash(__name__)
server = app.server

fig = px.line(x=[1,2,3], y=[1,3,2], title="Hello, Dash")

app.layout = html.Div([
    html.H1("Minimal Dash"),
    dcc.Graph(figure=fig),
    # html.Div([
    #     html.H2("this is div with h2")
    # ])
])
if __name__ == "__main__":
    app.run(debug=True)