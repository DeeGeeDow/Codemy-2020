import pandas as pd 

df = pd.read_csv("problem-6-1.csv")

print(df.loc[df["maskapai"] == "country link"]["harga"].mean())