# myFile = open("fruits.txt")
# data = myFile.read()
# myFile.close()

with open("fruits.txt") as myFile:
    data = myFile.read()

print(data)