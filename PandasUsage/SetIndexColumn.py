import pandas

df = pandas.read_csv("Files/supermarkets.csv")
# df.set_index("ID", inplace=True)
df.set_index("State", inplace=True, drop=False)
print(df)
