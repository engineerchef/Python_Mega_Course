with open("files/vegetables.txt", "a+") as myFile:
    myFile.write("\nPotato")
    myFile.seek(0)
    data = myFile.read()

print(data)