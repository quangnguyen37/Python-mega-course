myfile = open("files/fruits.txt")

content = myfile.read()

myfile.close()

print (content)

with open("files/vegi.txt", "w") as myfile:
    myfile.write("kale\nTomato\nOnion")

print (content)