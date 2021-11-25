import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd

import plotly.graph_objs as go
from utils import Header, make_dash_table
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 4, Vectors
                    html.Div(
                        [
                            html.Div( #[html.Div([dcc.Input, dcc.Dropdown])] for i in range(0,10)
                                [
                                    [html.Div([dcc.Input(id = f'VV{i})', placeholder = "P", type = "text", value = "1")]) for i in range(0,10)]
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.Div([html.H6("Vector 2: "),
                                    dcc.Input(id='V2x',placeholder='Enter a value...',type='number',value=1),
                                    dcc.Input(id='V2y',placeholder='Enter a value...',type='number',value=2),
                                    dcc.Input(id='V2z',placeholder='Enter a value...',type='number',value=3)]),
                                ],
                                className="row",
                            ),
                            html.Br(),
                            html.Div([html.Div(id='Magn1'),html.Div(id='Magn2')], className="product"),
                            html.Br(),
                            html.Div([html.Div(id='dotprod'),html.Div(id='crossprod')], className="product"),
                        ],
                        className="row",
                        style={"margin-bottom": "5px"},
                    ),
                    # Row 5, Solo Matrices
                    html.Div(
                        [
                            html.Div([html.H6(["Matrix"], className="subtitle padded"),
                                    #html.Table(make_dash_table(df_fund_facts)),
                                    html.Div([html.H6("Single Matrix operation: "),
                                    dcc.Input(id='Matrix 1',placeholder='Enter in 1 2; 3 4 format',type='text',value="1 2; 3 4"),
                                    #dcc.Input(id='M1Rows',placeholder='Enter number of rows',type='number',value=2),
                                    #dcc.Input(id='M1Cols',placeholder='Enter number of cols',type='number',value=2)]),
                                    ],
                                    className="row",
                                    ),
                                ],
                            ),
                            html.Div(
                                [
                                    html.Label('What function do you want to perform?:'),
                                    dcc.Dropdown(id = 'DropdownSM',
                                    options=[
                                        {'label': 'Inverse (^-1)', 'value': 'inverse'},
                                        {'label': 'Transpose (^T)', 'value': 'transpose'},
                                        {'label': 'Determinant (D)', 'value': 'determinant'},
                                    ],
                                value = "transpose",
                                className="row"),
                                ]
                            ),
                            html.Br(),
                            html.Div(id='SMresult', className="product"),#'SMresult'
                            html.Br(),
                        ],
                        className="row ",
                    ),
                    # Row 6, Dual Matrices
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Matrices"], className="subtitle padded"),
                                    #html.Table(make_dash_table(df_fund_facts)),
                                    html.Div([html.H6("Dual Matrix operation: "),
                                    dcc.Input(id='Matrix 2',placeholder='Enter in 1 2; 3 4 format',type='text',value="1 2; 3 4"),
                                    #dcc.Input(id='M2Rows',placeholder='Enter number of rows',type='number',value=2),
                                    #dcc.Input(id='M2Cols',placeholder='Enter number of cols',type='number',value=2),
                                    dcc.Input(id='Matrix 3',placeholder='Enter in 1 2; 3 4 format',type='text',value="1 2; 3 4"),
                                    #dcc.Input(id='M3Rows',placeholder='Enter number of rows',type='number',value=2),
                                    #dcc.Input(id='M3Cols',placeholder='Enter number of cols',type='number',value=2)],
                                    ],
                                    ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.Label('What function do you want to perform?:'),
                                    dcc.Dropdown(id = 'DropdownDM',
                                    options=[
                                        {'label': 'Addition (+)', 'value': 'add'},
                                        {'label': 'Subtraction (-)', 'value': 'sub'},
                                        {'label': 'Multiplication (x)', 'value': 'mult'},
                                    ],
                                value = "add",
                                className="row"),
                                ]
                            ),
                            html.Br(),
                            html.Div(id = 'DMresult', className="product"), #DMresult
                            html.Br(),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
