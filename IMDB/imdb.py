import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imdb_top_1000.csv')

#PROBLEM 1

director = input("Enter the name of the director")

grouped1_df = df.groupby('Director')['Series_Title']

print('The following are movies directed by ' + director)

for key, item in grouped1_df:

    if key == director:
        print(grouped1_df.get_group(key))

#PROBLEM 2

year = input("Enter a year")

df['Runtime'] = df['Runtime'].str.replace('min', " ").astype(int)

grouped2_df = df[(df['Released_Year'] == year) & (df['Runtime'] >= 120)].groupby(df['Series_Title'])

print("The following are movies that have been released in " + year + " and have runtimes that are over 120 minutes:")


for key, item in grouped2_df:

     print(key)


#PROBLEM 3

print("No. of movies by each director :")

pd.set_option("display.max_rows", None, "display.max_columns", None)

print(df['Director'].value_counts())





