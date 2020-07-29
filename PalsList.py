print("What is your name")
UserName = input()
ListOfFav = []

try:
    print("Hello! " + UserName +  "!  Welcome to Py World")
    print("Py want to know more about you")
    
    for i in range(4):
            print("who is your favorite actress?")
            MyFav = input()
            try:
                ListOfFav.append(MyFav)
            except:
                print("Please enter a valid value")

except:
    print("I think you do not want to be friendly with Py!")


if len(ListOfFav):
        print("Your fav are [" + str(ListOfFav)  + "]")
        print("Thanks for sharing this info")