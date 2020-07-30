palsnewList=["Jacquline", "Kirti", "Shraddha", "Iliana", "Kiara"]

print("Who is your favorite actress?")

try:
    tempActress = input()
    for i in range(len(palsnewList)):
        if tempActress == palsnewList[i]:
            print("Your favourite actress" + palsnewList[i] + "is stored in the " + str(i) + "Position of the list")
        else:
            print("Sorry!" + tempActress + "did not make it to the list")
    
except :
    print("I think you did not enter a valid value")
    print(palsnewList)


