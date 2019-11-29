import pandas as p
from geopy.geocoders import ArcGIS

nom = ArcGIS()
n = nom.geocode("3995 23rd St, San Francisco, CA 94114")
print("Longitude : {}, Latitude : {}".format(n.longitude, n.latitude))

df = p.read_json("../Files/supermarkets.json")
# print(df)

df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]
# print(df)

df["Coordinates"] = df["Address"].apply(nom.geocode)
# print(df.Coordinates)
# print(df.Coordinates[0])
# print(df.Coordinates[0].latitude)

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)
