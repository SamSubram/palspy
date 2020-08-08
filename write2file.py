#Create a file with name Animals.txt and write some text
'''with open("Animals.txt", "w") as myFile:
    myFile.write("List of animals: \n")
    myFile.write(" Elephant\n Zebra\n Croc\n Horse\n Buffalo\n Jiraffe\n Leopard\n Lion\n Tiger\n Kangaroo\n")
'''

#Read first 90 characters of the file Cities.txt and write into first.txt
'''
with open("Cities.txt") as myFile:
    content = myFile.read()

with open("first.txt", "w") as myFile:
    myFile.write(content[:90])
'''

with open("Fruits.txt") as myFile:
    content = myFile.read()

with open("Animals.txt", "a") as myFile:
    myFile.write(content)

print("content added to bear2.txt is \n" + content)