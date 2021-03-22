import pandas as pd

users = pd.read_csv("users.csv")
purchases = pd.read_csv("purchases.csv")

users.head()
purchases.head()

df = purchases.merge(users, how="left", on="uid")

agg_df = df.groupby(["country","device","gender","age"]).agg({"price": "sum"}).sort_values("price",ascending=False)

agg_df.head()
agg_df.reset_index(inplace=True)

mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["age"].max())]
agg_df["age_cat"] = pd.cut(agg_df["age"], bins=[0, 18, 24, 31, 41, agg_df["age"].max()], labels=mylabels)

agg_df["customers_level_based"] = [col[0] + "_" + col[1].upper() + "_" + col[2] + "_" + col[5] for col in agg_df.values]


agg_df = agg_df.groupby("customers_level_based").agg({"price": "mean"})
agg_df.reset_index(inplace=True)

agg_df["segment"] = pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])

agg_df.head()