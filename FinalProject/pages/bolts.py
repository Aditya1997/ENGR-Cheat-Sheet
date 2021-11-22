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
dfboltsimp.set_index('No. or Dia.', 'Number of Threads Per Inch')
dfboltsmet = pd.read_csv(r"C:\Users\adity\Documents\GitHub\ENGR-Cheat-Sheet\FinalProject\data\boltsizingmetric.csv")
dfboltsmet.set_index('Tap size', 'Threads per mm')

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
                                [html.Label('Number or Diameter Threads per Inch'),
                                dcc.Dropdown(id = "ImpUD",
                                options=[{'label': i, 'value': i} for i in pd.unique(dfboltsimp['No. or Dia.'].values.ravel('K'))],
                                value = "0",
                                className="five columns"),
                                #html.Label('Threads per Inch'),
                                dcc.Dropdown(id = "ImpThreads",
                                options=[{'label': i, 'value': i} for i in pd.unique(dfboltsimp['Number of Threads Per Inch'].values.ravel('K'))],
                                value = "56",
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
                                style={"margin-bottom": "20px"},
                            )
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
                                    [html.H5("Bolts Table (Metric)"),
                                    html.Br([]), # This adds a line break
                                    html.Table(make_dash_table(dfboltsmet))],
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 3, NA
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     ["Vectors"], className="subtitle padded"
                    #                 ),
                    #                 #html.Table(make_dash_table(df_fund_facts)),
                    #                 html.Div([html.H6("Vector 1: "),
                    #                 dcc.Input(id='V1x',placeholder='Enter a value...',type='number',value=1),
                    #                 dcc.Input(id='V1y',placeholder='Enter a value...',type='number',value=2),
                    #                 dcc.Input(id='V1z',placeholder='Enter a value...',type='number',value=3)]),
                    #             ],
                    #             className="row",
                    #         ),
                    #         html.Div(
                    #             [
                    #                 html.Div([html.H6("Vector 2: "),
                    #                 dcc.Input(id='V2x',placeholder='Enter a value...',type='number',value=1),
                    #                 dcc.Input(id='V2y',placeholder='Enter a value...',type='number',value=2),
                    #                 dcc.Input(id='V2z',placeholder='Enter a value...',type='number',value=3)]),
                    #             ],
                    #             className="row",
                    #         ),
                    #         html.Br(),
                    #         html.Div(id='dotprod', className="product"),
                    #         html.Br(),
                    #     ],
                    #     className="row",
                    #     style={"margin-bottom": "5px"},
                    # ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
