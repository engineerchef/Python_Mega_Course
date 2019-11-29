import pandas

df = pandas.read_csv("Files/data.txt",  header=None)
df.columns = ["ID", "Address", "City", "State", "Country", "Name", "Employees"]
print(df)
