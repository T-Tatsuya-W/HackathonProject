import pandas as pd
def generator():
    from random import randint

    df = pd.read_csv("Constructor/DataSet_UniqueIDs.csv")
    N = len(df)
    row = df.iloc[randint(0, N-1)] 

    name = row["Name"]
    _id = row["ID"]
    sport = row["Sport"]
    age = row["Age"]
    team = row["Team"]
    medal = row["Medal"]
    year = row["Year"]



    afterQuote = f"{name} \n{age} years old {medal} medalist in {sport} from {team} "
    return afterQuote
