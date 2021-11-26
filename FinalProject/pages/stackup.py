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
                    # Collecting dims/tols
                    html.Div(
                        [
                            html.Div( #[html.Div([dcc.Input, dcc.Dropdown])] for i in range(0,10)
                                [
                                    html.Div([dcc.Dropdown(id = f'S{i}', value = '',
                                    options=[
                                        {'label': '+', 'value': '+'},
                                        {'label': '-', 'value': '-'}], className = "three columns"),
                                    dcc.Input(id = f'D{i}', placeholder = f"Dimension {i}", value = '', type = "text", className = "three columns"),
                                    dcc.Dropdown(id = f'tolS{i}', value = '',
                                    options=[
                                       {'label': '+', 'value': '+'},
                                       {'label': '-', 'value': '-'},
                                       {'label': '±', 'value': '+-'}], className = "three columns"),
                                    dcc.Input(id = f'tolD{i}', placeholder = f"Tolerance {i}", value = '', type = "text", className = "three columns")
                                    ],
                                    className = "row"
                                    )
                                    for i in range(0,10) # maximum of 10 stackup dims
                                ],
                                className="row",
                            ),
                        ],
                    ),
                    # Tolerance Results
                    html.Div(
                        [
                            html.Div([html.H6(["Tolerance Results"], className="subtitle padded"),
                                    html.Div(id='nomGap'),
                                    html.Div(id='minGap'),
                                    html.Div(id='maxGap'),
                                    #dcc.Input(id='M1Rows',placeholder='Enter number of rows',type='number',value=2),
                                    #dcc.Input(id='M1Cols',placeholder='Enter number of cols',type='number',value=2)]),
                                    ],
                                    className="product",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
