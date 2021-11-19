# -*- coding: utf-8 -*-
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
#import dash_design_kit as ddk
from pages import (
    overview,
    centroid,
    bolts,
    gears,
    electronics,
    materials,
    finance,
    probability,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Engineering Calculators"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/centroid": #price-performance
        return centroid.create_layout(app)
    elif pathname == "/dash-financial-report/screws":
        return bolts.create_layout(app)
    elif pathname == "/dash-financial-report/gears":
        return gears.create_layout(app)
    elif pathname == "/dash-financial-report/electronics":
        return electronics.create_layout(app)
    elif pathname == "/dash-financial-report/materials":
        return materials.create_layout(app)
    elif pathname == "/dash-financial-report/finance":
        return finance.create_layout(app)
    elif pathname == "/dash-financial-report/probability":
        return probability.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            overview.create_layout(app),
            centroid.create_layout(app),
            bolts.create_layout(app),
            gears.create_layout(app),
            electronics.create_layout(app),
            materials.create_layout(app),
            finance.create_layout(app),
            probability.create_layout(app)
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
