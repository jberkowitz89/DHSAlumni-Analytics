#packages
import pandas as pd
from espn_api.football import League

def get_league(league_id, year, swid, espn_s2):
    '''Helper function for getting league object'''
    league = League(league_id=league_id, year=year, swid=swid, espn_s2=espn_s2)
    return league


def get_teams_df(years):
    '''Function for getting list of teams in league each year'''

    teams_df = pd.DataFrame(columns=['team_id', 'team_name', 'owner_name', 'year'])
    team_ids = []
    team_names = []
    owners = []
    year_nums = []
    for year in years:
        league = get_league(league_id=league_id, year=year, swid=swid, espn_s2=espn_s2)
        teams = league.teams
        for team in teams:
            team_ids.append(team.team_id)
            team_names.append(team.team_name)
            owners.append(team.owner)
            year_nums.append(league.year)

    teams_df['team_id'] = team_ids
    teams_df['team_name'] = team_names
    teams_df['owner_name'] = owners
    teams_df['year'] = year_nums

    return teams_df


def get_drafts_df(years):
    '''Function for getting draft history dataframe'''

    cols = ['round_num', 'round_pick', 'player_id', 'player_name', 'team_id', 'year']
    drafts_df = pd.DataFrame(columns=cols)
    round_nums = []
    round_picks = []
    player_ids = []
    player_names = []
    team_ids = []
    year_nums = []

    for year in years:
        league = get_league(league_id=league_id, year=year, swid=swid, espn_s2=espn_s2)
        draft = league.draft

        for pick in draft:
            round_nums.append(pick.round_num)
            round_picks.append(pick.round_pick)
            player_ids.append(pick.playerId)
            player_names.append(pick.playerName)
            team_ids.append(pick.team.team_id)
            year_nums.append(league.year)

    drafts_df['round_num'] = round_nums
    drafts_df['round_pick'] = round_picks
    drafts_df['player_id'] = player_ids
    drafts_df['player_name'] = player_names
    drafts_df['team_id'] = team_ids
    drafts_df['year'] = year_nums

    return drafts_df

