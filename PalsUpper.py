import random

myStr = "test"
print("Enter a string which you would like to convert to upper")
try:
    myStr = input()
    if(myStr.isalpha()):
        print("Your required string is:" + "\n" + myStr.upper())
    else:
        print("Your input has invalid values")
except:
    print("Something went wrong. Apologies!")
    
        
