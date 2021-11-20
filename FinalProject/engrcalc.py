# -*- coding: utf-8 -*-
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
from numpy import linalg
import pandas as pd
#import dash_design_kit as ddk
from pages import (
    overview,
    centroid,
    bolts, # pandas df
    gears,
    electronics, # resistor code df?
    materials, # pandas df
    finance,
    probability
)
from callbacks import *

app = dash.Dash(
    __name__, suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width"}], # We add suppress_callback_exceptions=True to avoid the callback exceptions for functions
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
    if pathname == "/FinalProject/price-performance": # centroid, this link must correspond to href in header in utils.py
        return centroid.create_layout(app)
    elif pathname == "/FinalProject/bolts":
        return bolts.create_layout(app)
    elif pathname == "/FinalProject/gears":
        return gears.create_layout(app)
    elif pathname == "/FinalProject/electronics":
        return electronics.create_layout(app)
    elif pathname == "/FinalProject/materials":
        return materials.create_layout(app)
    elif pathname == "/FinalProject/finance":
        return finance.create_layout(app)
    elif pathname == "/FinalProject/probability":
        return probability.create_layout(app)
    elif pathname == "/FinalProject/full-view":
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

##################################### CALLBACKS for basic functions

@app.callback(
    Output('dotprod', 'children'),
    Input('V1x', 'value'),
    Input('V1y', 'value'),
    Input('V1z', 'value'),
    Input('V2x', 'value'),
    Input('V2y', 'value'),
    Input('V2z', 'value'),
)
def dot_product(V1x, V1y, V1z, V2x, V2y, V2z):
    V1 = np.array([V1x, V1y, V1z])
    V2 = np.array([V2x, V2y, V2z])
    x = np.dot(V1,V2)
    return 'Dot Product: {}'.format(x)

@app.callback(
    Output('SMresult', 'children'),
    Input('Matrix1', 'value'),
    Input('DropdownSM', 'value'),
)
def SMoperation(M1, DSM):
    a = np.matrix(M1)
    if DSM == "inverse":
        try:
            ainv = np.linalg.inv(a)
            return ainv
        except:
            return "The matrix does not have an inverse"
    if DSM == "transpose":
        M1T = np.transpose(M1)
        return M1T
    if DSM == "determinant":
        try:
            det = np.linalg.det(M1)
            return det
        except:
            return "The matrix does not have a determinant"
        return det

@app.callback(
    Output('DMresult', 'children'),
    Input('Matrix2', 'value'),
    Input('Matrix3', 'value'),
    Input('DropdownDM', 'value'),
)
def DMoperation(M1, M2, DDM):
    a = np.matrix(M1)
    b = np.matrix(M2)
    if DSM == "add":
        try:
            add = a + b
            return add
        except:
            return "The matrices cannot be added"
    if DSM == "sub":
        try:
            sub = a - b
            return sub
        except:
            return  "The matrices cannot be subtracted"
    if DSM == "transpose":
        try:
            mult = np.matmul(a,b)
            return mult
        except:
            return  "The matrices cannot be multiplied"


if __name__ == "__main__":
    app.run_server(debug=True) #dev_tools_ui=False,dev_tools_props_check=False
