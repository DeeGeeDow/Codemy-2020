import pandas as pd 

df = pd.read_csv("problem-6-1.csv")

print(len(df.loc[df["harga"] > 3500000]))