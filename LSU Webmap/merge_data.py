import pandas as pd
import state_abbreviations

#Import the datasets to be merged
roster_df = pd.read_csv("lsu_roster.csv", "*", header=0)
cities_df = pd.read_csv("worldcities.csv")

#Subset the data to only include the USA as retain only the necessary variables for WebMap
cities_df = cities_df[cities_df['iso3'] == 'USA']
cities_df = cities_df[['city', 'admin_name', 'lat', 'lng']]

#Grab the city and state since the High School was included in the variable string
roster_df['city'] = roster_df['city'].apply(lambda city: city.split('(')[0].strip())

#In order to merge the two data sets, the states must both be abbrevatiated.  A custom function 
#was created to abbreviate the states.  
cities_df['admin_name'] = cities_df['admin_name'].apply(lambda x: state_abbreviations.abbreviateState(x))

#Manipulate the city variable in cities_df to match the city variable from the roster_df
cities_df['city'] = cities_df['city'] + ', ' + cities_df['admin_name']

#Merge the datasets by city
new_df = pd.merge(cities_df, roster_df, on="city")
print(new_df.head(10))

#Export to csv
new_df.to_csv('lsu_merged.csv')