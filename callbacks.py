import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
from engrcalc import app

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
