import pandas

df = pandas.read_json("Files/supermarkets.json")

# Adding New Column as 'Continent'
df["Continent"] = df.shape[0] * ["North America"]
print(df)

print()

# Updating An Existing 'Country' Column with 'South America'
df["Continent"] = df["Country"] + "," + "South America"
print(df)

# Transposing all table
print(df.T)
