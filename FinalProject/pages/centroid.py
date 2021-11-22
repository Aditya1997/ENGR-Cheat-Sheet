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

dimoptions = {
    'C': ['Radius'],
    'R': ['Length', 'Height'],
    'S': ['Side Length'],
    'I': ['Top Flange Width', 'Top Flange Thickness', 'Beam Height','Web Thickness','Bottom Flange Width', 'Bottom Flange Thickness'],

}

dimoptionsC = ['Radius']

dimoptionsR = ['Length', 'Height']

dimoptionsS = ['Side Length']

dimoptionsI=['Top Flange Width', 'Top Flange Thickness', 'Beam Height','Web Thickness','Bottom Flange Width', 'Bottom Flange Thickness']

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
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
                                ]),
                            html.Div(
                                [
                                    html.Div(id='DimString'),
                                ]),
                            html.Div(
                                    [dcc.Input(id = "D{}".format(k), type = 'number', placeholder="Dim {}".format(k),value=1) for k in range(1,7)],#range(1,7)
                                    #for i in dcc.Store(id='DimParam'):
                                    #    dcc.Input(id = f'D{i.index}', placeholder = i)
                                    #[dcc.Input(id = "D{}".format(k), type = 'number', placeholder="Dim {}".format(k),value=1) for k in ]#
                            ),
                        ],
                        className="row"
                    ),
                    html.Div(
                        [
                            html.Div(id='Centroid'),
                            html.Div(id="Area")
                        ],
                    className = "row"),
                    # # Row 2
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6("Performance", className="subtitle padded"),
                    #                 dcc.Graph(
                    #                     id="graph-4",
                    #                     figure={
                    #                         "data": [
                    #                             go.Scatter(
                    #                                 x=df_graph["Date"],
                    #                                 y=df_graph["Calibre Index Fund"],
                    #                                 line={"color": "#97151c"},
                    #                                 mode="lines",
                    #                                 name="Calibre Index Fund",
                    #                             ),
                    #                             go.Scatter(
                    #                                 x=df_graph["Date"],
                    #                                 y=df_graph[
                    #                                     "MSCI EAFE Index Fund (ETF)"
                    #                                 ],
                    #                                 line={"color": "#b5b5b5"},
                    #                                 mode="lines",
                    #                                 name="MSCI EAFE Index Fund (ETF)",
                    #                             ),
                    #                         ],
                    #                         "layout": go.Layout(
                    #                             autosize=True,
                    #                             width=700,
                    #                             height=200,
                    #                             font={"family": "Raleway", "size": 10},
                    #                             margin={
                    #                                 "r": 30,
                    #                                 "t": 30,
                    #                                 "b": 30,
                    #                                 "l": 30,
                    #                             },
                    #                             showlegend=True,
                    #                             titlefont={
                    #                                 "family": "Raleway",
                    #                                 "size": 10,
                    #                             },
                    #                             xaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     "2007-12-31",
                    #                                     "2018-03-06",
                    #                                 ],
                    #                                 "rangeselector": {
                    #                                     "buttons": [
                    #                                         {
                    #                                             "count": 1,
                    #                                             "label": "1Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 3,
                    #                                             "label": "3Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "count": 5,
                    #                                             "label": "5Y",
                    #                                             "step": "year",
                    #                                         },
                    #                                         {
                    #                                             "count": 10,
                    #                                             "label": "10Y",
                    #                                             "step": "year",
                    #                                             "stepmode": "backward",
                    #                                         },
                    #                                         {
                    #                                             "label": "All",
                    #                                             "step": "all",
                    #                                         },
                    #                                     ]
                    #                                 },
                    #                                 "showline": True,
                    #                                 "type": "date",
                    #                                 "zeroline": False,
                    #                             },
                    #                             yaxis={
                    #                                 "autorange": True,
                    #                                 "range": [
                    #                                     18.6880162434,
                    #                                     278.431996757,
                    #                                 ],
                    #                                 "showline": True,
                    #                                 "type": "linear",
                    #                                 "zeroline": False,
                    #                             },
                    #                         ),
                    #                     },
                    #                     config={"displayModeBar": False},
                    #                 ),
                    #             ],
                    #             className="twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                    # # Row 3
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     [
                    #                         "Average annual returns--updated monthly as of 02/28/2018"
                    #                     ],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 html.Div(
                    #                     [
                    #                         html.Table(
                    #                             make_dash_table(df_avg_returns),
                    #                             className="tiny-header",
                    #                         )
                    #                     ],
                    #                     style={"overflow-x": "auto"},
                    #                 ),
                    #             ],
                    #             className="twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                    # # Row 4
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     [
                    #                         "After-tax returns--updated quarterly as of 12/31/2017"
                    #                     ],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 html.Div(
                    #                     [
                    #                         html.Table(
                    #                             make_dash_table(df_after_tax),
                    #                             className="tiny-header",
                    #                         )
                    #                     ],
                    #                     style={"overflow-x": "auto"},
                    #                 ),
                    #             ],
                    #             className=" twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                    # # Row 5
                    # html.Div(
                    #     [
                    #         html.Div(
                    #             [
                    #                 html.H6(
                    #                     ["Recent investment returns"],
                    #                     className="subtitle padded",
                    #                 ),
                    #                 html.Table(
                    #                     make_dash_table(df_recent_returns),
                    #                     className="tiny-header",
                    #                 ),
                    #             ],
                    #             className=" twelve columns",
                    #         )
                    #     ],
                    #     className="row ",
                    # ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
