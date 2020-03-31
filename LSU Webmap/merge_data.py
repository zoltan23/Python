import pandas as pd

roster_df = pd.read_csv("lsu_roster.csv", "*", header=0)
cities_df = pd.read_csv("worldcities.csv")

#Extract just the city

roster_df['city'] = roster_df['city'].apply(lambda city: city.split()[:2])

print(roster_df['city'])