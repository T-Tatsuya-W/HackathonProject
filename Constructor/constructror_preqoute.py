
# import csv
# def constructor():
#     with open('DataSet_UniqueIDs.csv') as csvfile:
#         spamreader = csv.reader(csvfile)
#         # Math.floor(Math.random() * max)
#         item =[]
#         for line in spamreader:
#             item.append(line)

#         print(item)
# constructor()

import pandas as pd
from random import randint
#df: data frame: think of it s a list of dictionarry
df = pd.read_csv("Constructor/DataSet_UniqueIDs.csv")
N = len(df)
row = df.iloc[randint(0, N-1)] #
# row: a dictionary that has filednam: data
# for _, rrow in df[df['Age'] > 25].iterrows():
#     pass


# print(df.columns)
# print(row, row["Name"])

name = row["Name"]
_id = row["ID"]
sport = row["Sport"]
age = row["Age"]
team = row["Team"]
medal = row["Medal"]
year = row["Year"]


# print(f"{name} who competed in {sport}")
afterQuote = f"{age} years old {medal} medalist in {sport} from {team} "
print(afterQuote)