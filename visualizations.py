import plotly.express as px
from tables import team_points_by_week_table


def team_points_by_week_chart():
    df = team_points_by_week_table()
    chart = px.line(df, x="Week", y="Points", color="Team")
    return chart
