import pandas as pd 

df = pd.read_csv("problem-6-1.csv")

print(len(df.loc[(df["tahun"] == 2014) & (df["asal"] != "PDG") & (df["tujuan"] != "PDG")]))