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

dfboltsimp = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingimp.csv", skiprows=7)
dfboltsmet = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv")

def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                html.Div(
                    [
                    # Imperial
                    html.Div(
                        [
                            html.Div(
                                    [html.H5("Bolts Table (Imperial)"),
                                    html.Br([]), # This adds a line break
                                    html.Table(make_dash_table(dfboltsimp))],
                                    ),
                                ],
                                className="product",
                    ),
                    # Imperial lookup
                    html.Div(
                        [
                            html.Div(
                                [html.Label('Number or Diameter'),
                                dcc.Dropdown(id = "ImpUD",
                                options=[{'label': i, 'value': str(i)} for i in pd.unique(dfboltsimp['No. or Dia.'].values.ravel('K'))],
                                value = '1',
                                className="five columns"),
                                # html.Label('Threads per Inch'),
                                # dcc.Dropdown(id = "ImpThreads",
                                # options=[{'label': i, 'value': i} for i in pd.unique(dfboltsimp['Number of Threads Per Inch'].values.ravel('K'))],
                                # value = "56",
                                # className="five columns"),
                                ],
                                className="row",
                                style={"margin-bottom": "20px"},
                            ),
                            html.Div(
                                [html.Label('Threads per Inch'),
                                dcc.Dropdown(id = "ImpThreads",
                                options=[{'label': i, 'value': i} for i in pd.unique(dfboltsimp['Number of Threads Per Inch'].values.ravel('K'))],
                                value = 72,
                                className="five columns"),
                                ],
                                className="row",
                                style={"margin-bottom": "20px"},
                            )
                        ]
                    ),
                    # Imperial lookup result
                    html.Div(
                        [
                            html.Div(
                                [html.Div(id='impresult', className="product")
                                ],
                                className="row",
                                style={"margin-bottom": "20px"})
                        ]
                    ),
                    # Metric
                    html.Div(
                        [
                            html.Div(
                                    [html.H5("Bolts Table (Metric)"),
                                    html.Br([]), # This adds a line break
                                    html.Table(make_dash_table(dfboltsmet))],
                                    ),
                        ],
                        className="product",
                    ),
                    # Metric lookup
                    html.Div(
                        [
                            html.Div(
                                [html.Label('Tap Size'),
                                dcc.Dropdown(id = "TapSize",
                                options=[{'label': i, 'value': str(i)} for i in pd.unique(dfboltsmet['Tap size'].values.ravel('K'))],
                                value = 'M3x.05',
                                className="five columns"),
                                ],
                                className="row",
                                style={"margin-bottom": "20px"},
                            ),
                        ]
                    ),
                    # Metric lookup result
                    html.Div(
                        [
                            html.Div(
                                [html.Div(id='metresult', className="product")
                                ],
                                className="row",
                                style={"margin-bottom": "20px"},
                            )
                        ]
                    ),
                ],
            ),
        ],
        className="sub_page",
        )
    ],
    className="page",
)
