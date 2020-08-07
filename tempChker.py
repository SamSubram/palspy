# Get user input of temperature and display a message - SamSubram
def tempChker(currTemp):
    if currTemp > 7:
        return 'Warm'
    else:
        return 'Cold'
        

localTemp =0
print('Enter temperature in your city')
try:
    localTemp = int(input())
    if(tempChker(localTemp) == 'Warm'):
        print("Great! your city is warmer")
        print(type(localTemp))

    elif(tempChker(localTemp) == 'Cold'):
        print("Cool! you live in a cooler city")
        print(type(localTemp))

    else:
        print("unable to determine! Are you from Earth?")
        print(type(localTemp))    

except:
    print("Unknown Error!Are you from Earth?")
    print(type(localTemp))

## Display the category based on user input temperature
''' Code to check later
def tempChk(currTemp):
    if currTemp > 25:
        return 'Hot'
    elif currTemp >= 15 and currTemp <= 25:
        return 'warm'
    else:
        return 'Cold'

currTemp = 30   
print("you place is" + tempChk(currTemp)) '''


#### Convert the user input to Title(First letter in caps)
'''def userGreet(user_name):
   return("Hi %s" % user_name)

#user_input = input("Please enter your name")
print(userGreet("Marie"))'''

#
'''def userTitle(uname):
    return ("Hi " + uname.title())
    

print (userTitle("Sam"))
'''

## Looping through Dictionary
'''phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for item in phone_numbers.items():
    print(item[0] + ": " +item[1]) '''

###
