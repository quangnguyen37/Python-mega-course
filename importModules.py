import time
import os 
import pandas

while True:
    if os.path.exists("files/vegi.txt"):
        with open("files/vegi.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)