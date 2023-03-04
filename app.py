from dash import Dash, callback, html, dcc
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import matplotlib as mpl
import gunicorn  # whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server
from whitenoise import WhiteNoise  # for serving static files on Heroku
from dash import Dash, html, dcc
import plotly.express as px
from espn_api.football import League

# Instantiate dash app
app = Dash(__name__)

league = League(
    league_id=57605111,
    year=2022,
    espn_s2="AEBljLTvAWQpfgm071iZfMNA%2FzfweMFw2Ph1IZEOka3wjXos0vLrjA5gi1ls739ioa6FQCTwA9PE6o12qVzuof%2BYEnoJ0SDbSoXlvpAbYQjQIogEi0qlazZ%2Bm0zP8Xsn%2BE6Fh39ImDCUgVto0mitLZU6efBNze7QqMC2giomtIKGTe4bJJ9G4boqtaU5144PB5MnvEuLnRZx2py2GmXwKscFL6dNiOEFpsC1f4dozu8tw0cjnJdjtQOaPzKAGsWdUrR62CpWtAPcGngtB5My7Rga",
    swid="{1124F5EB-909C-4747-A269-E0C8729AF9C9}",
)

team_standings = {}
for team in league.teams:
    team_standings[team.team_name] = team.final_standing

standings = (
    pd.DataFrame.from_dict(team_standings, orient="index", columns=["Final Standing"])
    .reset_index()
    .sort_values(by="Final Standing", ascending=False)
)

lame_bar_chart = px.bar(standings, x="index", y="Final Standing")

app.layout = html.Div(
    children=[
        html.H1(children="First Pass"),
        html.Div(
            children="""
        Sample subtitle.
    """
        ),
        dcc.Graph(id="first-graph", figure=lame_bar_chart),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
