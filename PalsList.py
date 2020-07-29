print("What is your name")
UserName = input()
ListOfFav = [""]

try:
    print("Hello! " + UserName +  "!  Welcome to Py World")
    print("Py want to know more about you")
    for i in range(4):
        print("who is your favorite actress?")
        ListOfFav.append(input())
        print("Your favorite actresses are" + ListOfFav)
        print("Thanks for sharing this info")
    


except:
    print("I think you do not want to be friendly with Py!")