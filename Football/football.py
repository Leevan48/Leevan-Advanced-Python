import pandas as pd

df = pd.read_csv('european_soccer.csv')

# PROBLEM 1: HOW MANY TIMES TWO CLUBS HAVE PLAYED AGAINST EACH OTHER

team1 = input("Enter team one's name: ")
team2 = input("Enter team two's name: ")

counter1= df[(df['HomeTeam'] == team1) & (df['AwayTeam'] == team2)].shape
counter2= df[(df['HomeTeam'] == team2) & (df['AwayTeam'] == team1)].shape

frequency = counter1[0] + counter2[0]

print(team1 + " has played " + team2 + " on " + str(frequency) + " different ocassions")


#PROBLEM 2: HOW MANY GOALS A TEAM SCORED

team = input("Enter a team name: ")

df['FTHG'] = df['FTHG'].astype(int)
df['FTAG'] = df['FTAG'].astype(int)

group1_df = df[(df['HomeTeam'] == team)].sum()
group2_df = df[(df['AwayTeam'] == team )].sum()

list1 = []
list2 = []

for key in group1_df:
    list1.append(key)

for key2 in group2_df:
    list2.append(key2)

x = list1[4]
y = list2[5]
goals = x + y

print(team + " has scored " + str(goals) + " goals")








