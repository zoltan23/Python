import pandas as pd
import state_abbreviations

roster_df = pd.read_csv("lsu_roster.csv", "*", header=0)
cities_df = pd.read_csv("worldcities.csv")

cities_df = cities_df[cities_df['iso3'] == 'USA']
cities_df = cities_df[['city', 'admin_name', 'lat', 'lng']]


roster_df['city'] = roster_df['city'].apply(lambda city: city.split('(')[0].strip())


cities_df['admin_name'] = cities_df['admin_name'].apply(lambda x: state_abbreviations.abbreviateState(x))


cities_df['city'] = cities_df['city'] + ', ' + cities_df['admin_name']

#Merge the datasets by city
new_df = pd.merge(cities_df, roster_df, on="city")
print(new_df)