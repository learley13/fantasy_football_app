from datetime import date
from webbrowser import BackgroundBrowser
from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
import dash_daq as daq

import plotly.express as px
import plotly.io as pio
from plotly import graph_objects as go
import pandas as pd

import visualizations as viz


dash.register_page(
    __name__, path="/"
)  # by setting the path to '/', it becomes the landing page.

card_color = "#42474C"
background_color = "black"  # 005086"
pio.templates.default = "plotly_dark"


def drawFigure(figure):
    return html.Div(
        [
            dcc.Graph(
                figure=figure.update_layout(
                    # template='plotly_dark',
                    plot_bgcolor=card_color,
                    paper_bgcolor=card_color,
                ),
                config={"displayModeBar": False},
            )
        ]
    )


# Text field
def drawText(text):
    return html.Div(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                html.H2(text),
                            ],
                            style={"textAlign": "center"},
                        )
                    ]
                )
            ),
        ]
    )


layout = html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(drawText("Home Page")),
            ],
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([drawFigure(viz.team_points_by_week_chart())], width=6),
                dbc.Col([drawFigure(viz.team_points_by_week_chart())], width=6),
            ],
        ),
        html.Br(),
    ]
)
