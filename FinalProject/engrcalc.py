# -*- coding: utf-8 -*-
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
from numpy import linalg
import pandas as pd
import math

from utils import make_dash_table
from pages import (
    overview,
    centroid,
    bolts, # pandas df
    stackup,
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
    if pathname == "/FinalProject/centroid": # this link must correspond to href in header in utils.py
        return centroid.create_layout(app)
    elif pathname == "/FinalProject/bolts":
        return bolts.create_layout(app)
    elif pathname == "/FinalProject/stackup":
        return stackup.create_layout(app)
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
            stackup.create_layout(app),
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


############################################################### Page 1 callbacks (matrices and vectors)

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
    return f'Cross Product: {x}'


################################## MATRICES


@app.callback(
    Output('SMresult', 'children'),
    Input('Matrix 1', 'value'),
    Input('DropdownSM', 'value'),
)
def SMoperation(M1, DSM):
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
)
def DMoperation(M2, M3, DDM):
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

############################################################### Page 2 callbacks (centroid)

dimoptions = {
    'C': ['Radius'],
    'R': ['Length', 'Height'],
    'S': ['Side Length'],
    'I': ['Top Flange Width', 'Top Flange Thickness', 'Beam Height','Web Thickness','Bottom Flange Width', 'Bottom Flange Thickness'],
}

@app.callback(
    Output('Centroid', 'children'),
    Output('Area', 'children'),
    Input('CShape', 'value'),
    Input('D1', 'value'),
    Input('D2', 'value'),
    Input('D3', 'value'),
    Input('D4', 'value'),
    Input('D5', 'value'),
    Input('D6', 'value'),
)
def centroidshape(CS, D1, D2, D3, D4, D5, D6):
    if CS == "C":
        A = math.pi*D1**2
        x = D1
        y = D1
    elif CS == "R":
        A = D1*D2
        x = D1/2
        y = D2/2
    elif CS == "S":
        A = D1**2
        x = D1/2
        y = D1/2
    elif CS == "I":
        A = D1*D2+D5*D6+(D3-D2-D6)*D4
        x = D1/2
        num = (D1*D2*(D3-D2/2))+((D3-D2-D6)*D4)*(D3/2)+(D5*D6*(D6/2))
        y = num/A
    return  f"Centroid (bottom left is 0,0): {x}, {y}", f"Area: {A}"


@app.callback(
    Output('DimString', 'children'),
    Input('CShape', 'value'),
)
def dimlistdetails(CS):
    dimlist = dimoptions[CS]
    finaldimlist = [f'Dim {dimlist.index(k)+1} = {k}' for k in dimlist]
    finaldimstring = ", ".join(finaldimlist)
    return finaldimstring

############################################################### Page 3 callbacks (bolts)

impboltstpi = {
    '#0': ['80'],
    '#1': ['64','72'],
    '#2': ['56','64'],
    '#3': ['48','56'],
    '#4': ['40','48'],
    '#5': ['40','44'],
    '#6': ['32','40'],
    '#8': ['32','36'],
    '#10': ['24','32'],
    '#12': ['24','28','32'],
    '1/4': ['20','28','32'],
    '5/16': ['18','24','32'],
    '3/8': ['16','24','32'],
    '7/16': ['14','20','28'],
    '1/2': ['13','20','28'],
    '9/16': ['12','18','24'],
    '5/8': ['11','18','24'],
    '11/16': ['24'],
    '3/4': ['13','20','28'],
    '13/16': ['20'],
    '7/8': ['9','14','20'],
    '15/16': ['20'],
    '1': ['8','12','20'],
    '1-1/16': ['8'],
    '1-1/8': ['7','12','18'],
    '1-3/16': ['18'],
    '1-1/4': ['7','12','18'],
    '1-5/16': ['18'],
    '1-3/8': ['6','12','18'],
    '1-7/16': ['18'],
    '1-1/2': ['6','12','18'],
    '1-9/16': ['18'],
    '1-5/8': ['18'],
    '1-11/16': ['18'],
    '1-3/4': ['5'],
}

dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=8, dtype={2:'object'}) # reads type of column 2 (third col) as string instead of float
dfboltsmet = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv")

# Chained callback starts
@app.callback(
    Output('ImpThreadOptions', 'options'), #output is of type options, NOT children
    Input('ImpUD', 'value'))
def set_thread_options(selected_size):
    return [{'label': i, 'value': i} for i in impboltstpi[selected_size]] # drop down only allows real size + thread combinations

@app.callback(
    Output('ImpThreadOptions', 'value'),
    Input('ImpThreadOptions', 'options'))
def set_thread_value(available_options):
    return available_options[0]['value'] # sets starting value to always be first in list of thread options, collects value of the 'value' key of first dictionary in list
# Chained callback ends

@app.callback(
    Output('impresult', 'children'),
    Input('ImpUD', 'value'),
    Input('ImpThreadOptions', 'value'),
)
def impresult(D,T):
    #dfx = dfboltsimp.set_index(['No. or Dia.', 'Number of Threads Per Inch']) # To set multindex
    #x = dfx.loc[(D,T),:] # loc[(D,T),:] to return values for all columns in the (D,T) multindex
    impres = dfboltsimp.loc[((dfboltsimp['No. or Dia.'] == D) & (dfboltsimp['Number of Threads Per Inch'] == T)),:] # this method of using loc produces a dataframe using a boolean mask
    #impres = dfboltsimp[((dfboltsimp['No. or Dia.']==D) & (dfboltsimp['Number of Threads Per Inch']==T))] # this method uses & to create a merged mask
    x = make_dash_table(impres)
    return x

@app.callback(
    Output('metresult', 'children'),
    Input('TapSize', 'value'),
)
def impresult(TapSize):
    impres = dfboltsmet.loc[((dfboltsmet['Tap size'] == TapSize)),:] # this method of using loc produces a dataframe using a boolean mask
    x = make_dash_table(impres)
    return x

############################################################### Page 3 callbacks (gears)


if __name__ == "__main__":
    app.run_server(debug=True) #dev_tools_ui=False,dev_tools_props_check=False
