import pandas

df = pandas.read_json("Files/supermarkets_deletedRowAndColumns.json")
# print(df.drop("City", 1))
# print(df.drop(df.index[0:3], 0))
# print(df.drop(df.columns[0:3], 1))
