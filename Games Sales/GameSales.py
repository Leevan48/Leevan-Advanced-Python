import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dato.csv')

print("No. of games per publisher :")
print(df['Publisher'].value_counts())

print("Game with maximum sales in Europe: ")


maximum_eu = df['EU_Sales'].max()


grouped1_df = df.groupby('EU_Sales')['Platform']

for key, item in grouped1_df:

    if key == maximum_eu:
        print(grouped1_df.get_group(key))



print("Game with maximum sales in North America: ")

maximum_na = df['NA_Sales'].max()

grouped2_df = df.groupby('NA_Sales')['Platform']

for key, item in grouped2_df:

    if key == maximum_na:
        print(grouped2_df.get_group(key))





