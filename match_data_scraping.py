import pandas as pd

df = pd.read_html('https://fbref.com/en/comps/8/2023-2024/2023-2024-Champions-League-Stats',
                attrs={"id":"results2023-202480_overall"})[0]


df = df.dropna(subset=['Rk'])

print(df.head())