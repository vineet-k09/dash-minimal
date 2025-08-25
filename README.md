# Setup

## Virtual Env
```bash
# make a virtual environment
python -m venv venv

# activate it
```

## Installation
```bash
pip install dash plotly gunicorn
```

## Boiler Plate
```py
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)
server = app.server  # expose the server for deployment

# a toy figure; no data files, no pandas, just vibes
fig = px.line(x=[1, 2, 3], y=[1, 3, 2], title="Hello, Dash")

app.layout = html.Div([
    html.H1("Minimal Dash"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)  # dev server with hot reload
```

## Run
```bash
python app.py
```

## Deploy
### Create a Render “Web Service”

- Sign in to Render → New + → Web Service → connect your GitHub repo.

- Instance type: Free. (Yes, they still have a free tier suitable for hobby apps.) 

Start Command:
```bash
gunicorn app:server
```
(That tells Gunicorn to serve the Flask server exposed as server in app.py—the standard Dash deployment pattern.) 
GitHub

- Deploy. After the build finishes, Render gives you a public URL.