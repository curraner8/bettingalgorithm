import pandas as pd

df_23_24 = pd.read_html('https://fbref.com/en/squads/822bd0ba/2023-2024/matchlogs/all_comps/schedule/Liverpool-Scores-and-Fixtures-All-Competitions',
                  attrs={"id":"matchlogs_for"})[0]

data = ['Comp', 'Venue', 'Result', 'GF', 'GA', 'Opponent', 'xG', 'xGA']

df_23_24 = df_23_24[data]

#print(df_23_24)

df_22_23 = pd.read_html('https://fbref.com/en/squads/822bd0ba/2022-2023/Liverpool-Stats',
                        attrs={"id":"matchlogs_for"})[0]

df_22_23 = df_22_23[data]

#print(df_22_23)

df_21_22 = pd.read_html('https://fbref.com/en/squads/822bd0ba/2021-2022/Liverpool-Stats',
                        attrs={"id":"matchlogs_for"})[0]

df_21_22 = df_21_22[data]

#df = pd.concat([df_23_24, df_22_23, df_21_22])
df = pd.concat([df_21_22, df_22_23, df_23_24])

print(df)



def filter_matches(opponent):
    return df[df['Opponent'].str.contains(opponent)]

def avg_xg_vs(opponent):
    opponent_matches = df[df['Opponent'].str.contains(opponent)]
    total_xg = opponent_matches['xG'].sum()
    total_matches = opponent_matches['xG'].count()

    avg_xg = total_xg/total_matches
    return avg_xg

def avg_xga_vs(opponent):
    opponent_matches = df[df['Opponent'].str.contains(opponent)]
    total_xga = opponent_matches['xGA'].sum()
    total_matches = opponent_matches['xGA'].count()

    avg_xga = total_xga/total_matches
    return avg_xga

#CHELSEA VS LIVERPOOL
chelsea_liverpool = filter_matches('Chelsea')
print("Chelsea vs Liverpool:")
print(chelsea_liverpool)
xg_vs_chelsea = avg_xg_vs('Chelsea')
print("Avg xG against Chelsea:")
print(xg_vs_chelsea)
xga_vs_chelsea = avg_xga_vs('Chelsea')
print("Avg xGA:")
print(xga_vs_chelsea)

#ARSENAL VS LIVERPOOL
arsenal_liverpool = filter_matches('Arsenal')
print("Arsenal vs Liverpool:")
print(arsenal_liverpool)
xg_vs_arsenal = avg_xg_vs('Arsenal')
print('Avg xG against Arsenal:')
print(xg_vs_arsenal)
xga_vs_arsenal = avg_xga_vs('Arsenal')
print("Avg xGA:")
print(xga_vs_arsenal)

#MAN CITY VS LIVERPOOL
city_liverpool = filter_matches('Manchester City')
print("Man City vs Liverpool:")
print(city_liverpool)
xg_vs_city = avg_xg_vs('Manchester City')
print('Avg xG against City:')
print(xg_vs_city)
xga_vs_city = avg_xga_vs('Manchester City')
print("Avg xGA:")
print(xga_vs_city)

#MAN UNITED VS LIVERPOOL
united_liverpool = filter_matches('Manchester Utd')
print("Man United vs Liverpool:")
print(united_liverpool)
xg_vs_united = avg_xg_vs('Manchester Utd')
print("Avg xG against United:")
print(xg_vs_united)
xga_vs_united = avg_xga_vs('Manchester Utd')
print("Avg xGA:")
print(xga_vs_united)

#SPURS VS LIVERPOOL
spurs_liverpool = filter_matches('Tottenham')
print("Spurs vs Liverpool")
print(spurs_liverpool)
xg_vs_spurs = avg_xg_vs('Tottenham')
print("Avg xG against Spurs:")
print(xg_vs_spurs)
xga_vs_spurs = avg_xga_vs('Tottenham')
print("Avg xGA:")
print(xga_vs_spurs)

#EVERTON VS LIVERPOOL
everton_liverpool = filter_matches('Everton')
print("Everton vs Liverpool:")
print(everton_liverpool)
xg_vs_everton = avg_xg_vs('Everton')
print("Avg xG against Everton:")
print(xg_vs_everton)
xga_vs_everton = avg_xga_vs('Everton')
print("Avg xGA:")
print(xga_vs_everton)


#EXPECTED WIN PERCENTAGE

def expected_win_percentage(xg, xga, exponent=1.35):
    win_percentage = (xg ** exponent) / (xg ** exponent + xga ** exponent)
    return win_percentage

#VS EVERTON 
win_percentage_everton = expected_win_percentage(xg_vs_everton, xga_vs_everton)
print("Expected win percentage:")
print(win_percentage_everton)

#LOWER TABLE TEAMS
lower_table_opponents = ['Fulham', 'Brentford', 'Crystal Palace', 'Brighton', 'Wolves' ]

for opponent in lower_table_opponents:
    opponent_liv = filter_matches(opponent)
    print(f"{opponent} vs Liverpool:")
    print(opponent_liv)

    xg_for_liverpool = avg_xg_vs(opponent)
    print(f"Avg xG against {opponent}")
    print(xg_for_liverpool)

    xga_for_opponent = avg_xga_vs(opponent)
    print(f"Avg xGA for {opponent}:")
    print(xga_for_opponent)

    win_percentage =expected_win_percentage(xg_for_liverpool, xga_for_opponent)
    print(f"Expected win percentage vs {opponent}:")
    print(win_percentage)