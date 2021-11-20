import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd

import plotly.graph_objs as go
from utils import Header, make_dash_table
import pathlib
#import callbacks

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Engineering Calculators"),
                                    html.Br([]), # This adds a line break
                                    html.P(
                                        "\
                                    This webpage contains several engineering calculators for various \
                                    functions, including bolts, materials, and probabilities. This  \
                                    web app was developed using Plotly Dash, pandas, and numpy.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4, Vectors
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Vectors"], className="subtitle padded"
                                    ),
                                    #html.Table(make_dash_table(df_fund_facts)),
                                    html.Div([html.H6("Vector 1: "),
                                    dcc.Input(id='V1x',placeholder='Enter a value...',type='number',value=1),
                                    dcc.Input(id='V1y',placeholder='Enter a value...',type='number',value=2),
                                    dcc.Input(id='V1z',placeholder='Enter a value...',type='number',value=3)]),
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
                            html.Div(id='dotprod', className="product"),
                            html.Br(),
                        ],
                        className="row",
                        style={"margin-bottom": "5px"},
                    ),
                    # Row 5, Solo Matrices
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Matrices"], className="subtitle padded"
                                    ),
                                    #html.Table(make_dash_table(df_fund_facts)),
                                    html.Div([html.H6("Single matrix operation: "),
                                    dcc.Input(id='Matrix 1',placeholder='Enter in [1 2 3; 4 5 6; ...] format',type='text',value="[1 2;3 4]")]),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.Label('DropdownSM'),
                                    dcc.Dropdown(
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
                            html.Div(id='SMresult', className="product"),
                            html.Br(),
                        ],
                        className="row ",
                    ),
                    # Row 5, Dual Matrices
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Matrices"], className="subtitle padded"
                                    ),
                                    #html.Table(make_dash_table(df_fund_facts)),
                                    html.Div([html.H6("Dual Matrix operation: "),
                                    dcc.Input(id='Matrix 2',placeholder='Enter in [1 2 3; 4 5 6; ...] format',type='text',value="[1 2;3 4]"),
                                    dcc.Input(id='Matrix 3',placeholder='Enter in [1 2 3; 4 5 6; ...] format',type='text',value="[1 2;3 4]")]),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.Label('DropdownDM'),
                                    dcc.Dropdown(
                                    options=[
                                        {'label': 'Addition (+)', 'value': 'add'},
                                        {'label': 'Subtraction (-)', 'value': 'sub'},
                                        {'label': 'Multiplication (x)', 'value': 'mul'},

                                    ],
                                value = "add",
                                className="row"),
                                ]
                            ),
                            html.Br(),
                            html.Div(id='DMresult', className="product"),
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
