import pandas

df1 = pandas.read_csv("Files/supermarkets-commas.txt")
df1.set_index("ID")
print(df1)
print("=============================================================")

df2 = pandas.read_csv("Files/supermarkets-semi-colons.txt", sep=";")
df2.set_index("ID")
print(df2)
