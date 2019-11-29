import pandas

df1 = pandas.read_csv("Files/supermarkets.csv")
df1.set_index("ID")
print(df1)
