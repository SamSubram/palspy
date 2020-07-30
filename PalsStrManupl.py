

origstr = "Kat"
print("Kat in upper case: " + origstr.upper())
print("want to convert any string to Upper? Please let me know")
numbers = (0,1,2,3,4,5,6,7,8,9)
try:
    newstr = input()
    if  newstr.isalpha() == False:
            print("Your string has non string elements")
    else:
        print("Here you go: "  + newstr.upper())
except:
    print("Invalid input".upper())

