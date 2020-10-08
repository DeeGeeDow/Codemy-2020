import pandas as pd 

df = pd.read_csv("problem-6-1.csv")

macan = df.loc[df["maskapai"] == "macan"]

print(macan.loc[macan["harga"].idxmin()])