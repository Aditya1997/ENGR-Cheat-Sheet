# -*- coding: utf-8 -*-
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
from numpy import linalg
import pandas as pd

from utils import make_dash_table
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

############################################################################################### CALLBACKS for basic functions


############################################################### Page 1 callbacks

################################## VECTORS

@app.callback(
    Output('Magn1', 'children'),
    Output('Magn2', 'children'),
    Input('V1x', 'value'),
    Input('V1y', 'value'),
    Input('V1z', 'value'),
    Input('V2x', 'value'),
    Input('V2y', 'value'),
    Input('V2z', 'value'),
)
def magnitudecalc(V1x, V1y, V1z, V2x, V2y, V2z):
    V1 = np.array([V1x, V1y, V1z])
    V2 = np.array([V2x, V2y, V2z])
    M1 = np.linalg.norm(V1)
    M2 = np.linalg.norm(V2)
    return f'Magnitude Vector 1: {np.around(M1,5)}', f'Magnitude Vector 2: {np.around(M2,5)}'

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
    Output('crossprod', 'children'),
    Input('V1x', 'value'),
    Input('V1y', 'value'),
    Input('V1z', 'value'),
    Input('V2x', 'value'),
    Input('V2y', 'value'),
    Input('V2z', 'value'),
)
def cross_product(V1x, V1y, V1z, V2x, V2y, V2z):
    V1 = np.array([V1x, V1y, V1z])
    V2 = np.array([V2x, V2y, V2z])
    x = np.cross(V1,V2)
    return 'Cross Product: {}'.format(x)


################################## MATRICES


@app.callback(
    Output('SMresult', 'children'),
    Input('Matrix 1', 'value'),
    Input('DropdownSM', 'value'),
    #Input('M1Rows', 'value'),
    #Input('M1Cols', 'value')
)
def SMoperation(M1, DSM):# M1R, M1C
    #a = np.fromstring(M1, dtype=int, sep=' ').reshape(M1R, M1C)
    a = np.array(np.mat(M1), subok=True) # required format ('1 2; 3 4')
    places = 4
    if DSM == "inverse":
        try:
            ainv = np.linalg.inv(a)
            res = np.around(ainv,places).tolist()
            return f'Inverse: {[str(x) for x in res]}'
        except:
            return "The matrix does not have an inverse"
    elif DSM == "transpose":
        M1T = np.transpose(a)
        res = np.around(M1T,places).tolist()
        return f'Transpose: {[str(x) for x in res]}'
    elif DSM == "determinant":
        try:
            det = np.linalg.det(a)
            return f'Determinant ({places} places): {det:.4f}'
        except:
            return "The matrix does not have a determinant"

@app.callback(
    Output('DMresult', 'children'),
    Input('Matrix 2', 'value'),
    Input('Matrix 3', 'value'),
    Input('DropdownDM', 'value'),
    #Input('M2Rows', 'value'),
    #Input('M2Cols', 'value'),
    #Input('M3Rows', 'value'),
    #Input('M3Cols', 'value')
)
def DMoperation(M2, M3, DDM): #M2R, M2C,M3R, M3C
    #a = np.fromstring(M2, dtype=int, sep=' ').reshape(M2R, M2C)
    #b = np.fromstring(M3, dtype=int, sep=' ').reshape(M3R, M3C)
    a = np.array(np.mat(M2), subok=True) # required format ('1 2; 3 4')
    b = np.array(np.mat(M3), subok=True)
    places = 4
    if DDM == "add":
        try:
            add = a + b
            res = np.around(add,places).tolist()
            return f'Addition Result: {[str(x) for x in res]}'
        except:
            return "The matrices cannot be added"
    elif DDM == "sub":
        try:
            sub = a - b
            res = np.around(sub,places).tolist()
            return f'Subtraction Result: {[str(x) for x in res]}'
        except:
            return  "The matrices cannot be subtracted"
    elif DDM == "mult":
        try:
            mult = np.matmul(a,b)
            res = np.around(mult,places).tolist()
            return f'Multiplication Result: {[str(x) for x in res]}'
        except:
            return "The matrices cannot be multiplied"

############################################################### Page 2 callbacks

# @app.callback(
#     Output('CShapeOpt', 'children'),
#     Input('CShape', 'value'),
# )
# def centroidshape(CS):
#     dimoptions = {
#         'C': ['Radius'],
#         'R': ['Length', 'Height'],
#         'S': ['Side Length'],
#         'I': ['Flange Width', 'Flange Thickness', 'Beam Height','Web Thickness'],
#     }
#     if CS == "C":
#         return dimoptions["C"]
#     elif CS == "R":
#         return dimoptions["R"]
#     elif CS == "S":
#         return dimoptions["S"]
#     elif CS == "I":
#         return dimoptions["I"]
#
# x = centroidshape('C')
# print(x)

@app.callback(
    [Output('CShapeOpt_{}'.format(x), 'children') for x in range(1,5)],
    Input('CShape', 'value'),
)
def centroidshape(CS):
    dimoptions = {
        'C': ['Radius'],
        'R': ['Length', 'Height'],
        'S': ['Side Length'],
        'I': ['Flange Width', 'Flange Thickness', 'Beam Height','Web Thickness'],
    }
    if CS == "C":
        return dimoptions["C"]
    elif CS == "R":
        return dimoptions["R"]
    elif CS == "S":
        return dimoptions["S"]
    elif CS == "I":
        return dimoptions["I"]

############################################################### Page 3 callbacks

@app.callback(
    Output('impresult', 'children'),
    Input('ImpUD', 'value'),
    Input('ImpThreads', 'value'),
)

def impresult(D, T):
    dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
    #dfx = dfboltsimp.set_index(['No. or Dia.', 'Number of Threads Per Inch']) # To set multindex
    #x = dfx.loc[(D,T),:] # loc[(D,T),:] to returns values for everything in (D,T) index
    impres = dfboltsimp.loc[((dfboltsimp['No. or Dia.'] == D) & (dfboltsimp['Number of Threads Per Inch'] == T)),:] # this method of using loc produces a dataframe using a boolean mask
    #impres = dfboltsimp[((dfboltsimp['No. or Dia.']==D) & (dfboltsimp['Number of Threads Per Inch']==T))]
    x = make_dash_table(impres)
    return x

@app.callback(
    Output('metresult', 'children'),
    Input('TapSize', 'value'),
)

def impresult(TapSize):
    dfboltsmet = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv")
    impres = dfboltsmet.loc[((dfboltsmet['Tap size'] == TapSize)),:] # this method of using loc produces a dataframe using a boolean mask
    x = make_dash_table(impres)
    return x

if __name__ == "__main__":
    app.run_server(debug=True) #dev_tools_ui=False,dev_tools_props_check=False
