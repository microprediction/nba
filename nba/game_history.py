import pandas as pd



if __name__=='__main__':
    from nba_api.stats.static import teams
    from nba_api.stats.endpoints import leaguegamefinder
    import time

    nba_teams = teams.get_teams()
    all_games = None
    for team in nba_teams:
        print(team)
        gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team['id'])
        games = gamefinder.get_data_frames()[0]
        games.sort_values('GAME_DATE',inplace=True)
        print(len(games))
        if all_games is None:
            all_games = games
        else:
            all_games = pd.concat([all_games,games],ignore_index=True)
        time.sleep(1)
    all_games.to_csv('../data/games.csv')
    print(len(games))