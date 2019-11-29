import pandas

df1 = pandas.read_json("Files/supermarkets.json")
df1.set_index("ID")
print(df1)
