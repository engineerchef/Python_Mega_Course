import pandas as p

df = p.read_json("http://pythonhow.com/supermarkets.json")
df.set_index("Address")
# print(df.set_index("Address"))
# print(df.set_index("Address").loc["735 Dolores St":"332 Hill St", "Country":"ID"])
# print(df.loc["735 Dolores St":"332 Hill St", "Country":"ID"])
# print(df.loc["332 Hill St", "Country"])
# print(df.loc[:, "Country"])

# newList = list(df.loc[:, "Country"])
# print(newList)


# print(df.iloc[1:4, 1:4])
print(df.iloc[3, 1:4])
