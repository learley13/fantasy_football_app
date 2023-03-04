import pandas as pd

from espn_api.football import League

league = League(
    league_id=57605111,
    year=2022,
    espn_s2="AEBljLTvAWQpfgm071iZfMNA%2FzfweMFw2Ph1IZEOka3wjXos0vLrjA5gi1ls739ioa6FQCTwA9PE6o12qVzuof%2BYEnoJ0SDbSoXlvpAbYQjQIogEi0qlazZ%2Bm0zP8Xsn%2BE6Fh39ImDCUgVto0mitLZU6efBNze7QqMC2giomtIKGTe4bJJ9G4boqtaU5144PB5MnvEuLnRZx2py2GmXwKscFL6dNiOEFpsC1f4dozu8tw0cjnJdjtQOaPzKAGsWdUrR62CpWtAPcGngtB5My7Rga",
    swid="{1124F5EB-909C-4747-A269-E0C8729AF9C9}",
)


def team_summary_table():
    teams = {}
    for team in league.teams:
        team_info = {}
        team_info["abbrev"] = team.team_abbrev
        team_info["wins"] = team.wins
        team_info["losses"] = team.losses
        team_info["ties"] = team.ties
        team_info["points_for"] = team.points_for
        team_info["points_against"] = team.points_against
        team_info["acquisitions"] = team.acquisitions
        team_info["drops"] = team.drops
        team_info["trades"] = team.trades
        team_info["playoff_pct"] = team.playoff_pct
        team_info["projected_rank_after_draft"] = team.draft_projected_rank
        team_info["streak_type"] = team.streak_type
        team_info["streak_length"] = team.streak_length
        team_info["standing"] = team.standing
        teams[team.owner.split(" ", 1)[0]] = team_info
    df = pd.DataFrame(teams).T.sort_values(by="standing")
    return df


def team_points_by_week_table():
    teams = {}
    for team in league.teams:
        week_dict = {}
        for week, score in enumerate(team.scores):
            week_dict[week + 1] = score
            teams[team.owner.split(" ", 1)[0]] = week_dict
    df = (
        pd.DataFrame(teams)
        .reset_index()
        .rename(columns={"index": "Week"})
        .melt(id_vars=["Week"], value_name="Points", var_name="Team")
    )
    return df
