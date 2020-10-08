import pandas as pd 

df = pd.read_csv("problem-6-1.csv")

rjw = df.loc[df["maskapai"] == "rajawali"]
print((rjw.sort_values(["penumpang","harga"], ascending=[False,True])[:10]))