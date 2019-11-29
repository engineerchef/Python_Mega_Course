import time
import sys
import os

path = sys.prefix
print(path)
while True:
    if os.path.exists("files/vegetables.txt"):
        with open("files/vegetables.txt") as files:
            print(files.read())
    else:
        print("File does not exist!!!")
    time.sleep(5)