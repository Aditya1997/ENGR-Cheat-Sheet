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
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # row 1 (inputs)
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Centroid"], className="subtitle padded"
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    dcc.Dropdown(id = "CShape",
                                    options=[
                                        {'label': 'Circle', 'value': 'C'},
                                        {'label': 'Rectangle', 'value': 'R'},
                                        {'label': 'Square', 'value': 'S'},
                                        {'label': 'I-Beam', 'value': 'I'},
                                        ],
                                value = 'C',
                                className="row"),
                                ]
                            ),
                            html.Div(
                                [
                                    html.Label('Dimensions'),
                                    html.Div(id='DimString'),
                                ],
                                style={"font-size": "14px", "margin-top": "10px", "margin-bottom": "10px"},
                            ),
                            html.Div(
                                    [dcc.Input(id = "D{}".format(k), type = 'number', placeholder="Dim {}".format(k),value=1) for k in range(1,7)],#range(1,7)
                                    #for i in dcc.Store(id='DimParam'):
                                    #    dcc.Input(id = f'D{i.index}', placeholder = i)
                                    #[dcc.Input(id = "D{}".format(k), type = 'number', placeholder="Dim {}".format(k),value=1) for k in ]#
                            ),
                        ],
                        className="row"
                    ),
                    # row 2 (outputs)
                    html.Div(
                        [
                            html.Div(id='Centroid'),
                            html.Div(id="Area")
                        ],
                    className = "product"),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
