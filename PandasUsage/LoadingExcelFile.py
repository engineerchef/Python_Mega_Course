import pandas

df1 = pandas.read_excel("Files/supermarkets.xlsx", sheet_name=0)
df1.set_index("ID")
print(df1)
