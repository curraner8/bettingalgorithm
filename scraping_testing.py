import pandas as pd

df = pd.read_html('https://fbref.com/en/comps/9/2022-2023/2022-2023-Premier-League-Stats#all_league_summary',
                  attrs={"id":"results2022-202391_home_away"})[0]



full_data =['Squad', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'xG', 'xGD']

#drop the first level of multi index
df.columns = df.columns.droplevel(0)

#pick the specific columns
df = df[full_data]

teams_data = df.set_index('Squad').T.to_dict()

for team, stats in teams_data.items():
    print(f"{team}: {stats}")

print(df)

def get_team_data(teams, data):
    output = {team: data.get(team) for team in teams}
    return output

team_names = ['Arsenal', 'Liverpool']
matchup = get_team_data(team_names, teams_data)

for team, stats in matchup.items():
    print(f"{team}: {stats}")