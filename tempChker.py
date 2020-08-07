# Get user input of temperature and display a message - SamSubram
'''
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
'''
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
'''
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for val in phone_numbers.values():
    print("00" + val[1:])
'''

### String concatenation
'''
mydict = {}
i = 0
printStr = ""

while True:
    resp = input("Say something:")
    i = i+1
    # print(str(type(resp)) + " : " + resp )
    if(resp == '\\end'):
        break

    resp = resp.lower()

    if resp.startswith('how') or resp.startswith('why') or resp.startswith('what') or resp.startswith('how') or resp.startswith('where') or resp.startswith('when'):
        resp = resp +'?'
        mydict[i] = resp.capitalize()
  
    elif resp.startswith('do') or resp.startswith('is') or resp.startswith('can') or resp.startswith('may') or resp.startswith('was') or resp.startswith('could') or resp.startswith('did'):
        resp = resp +'? '
        mydict[i] = resp.capitalize()
    
    else:
        resp = resp + '. '
    
        # print("In else : " + resp.title())
        # mydict[i] = resp.title()
        mydict[i] = resp.capitalize()

  
    #print("User Input inside while:")
    # print(mydict)

for val in mydict.values():
  printStr = printStr+val

print(printStr)
'''
# print only decimals
def onlynums(iList):
    olist=[]
    for iVal in iList:
        try:
            if int(iVal) >= 0 or int(iVal)< 0:
                # print("Int in List: " + str(iVal))
                olist.append(int(iVal))
        except:
            # print("String " + str(iVal))
            # do nothing
            continue
    return olist

mylist=[]
inputStr=''

while True:
    if inputStr == 'end':
        break
    else:
        inputStr = input("Enter your list. Enter end if you are done: ")
        if inputStr !='end' and inputStr:
            mylist.append(inputStr)


# mylist =['delhi', 10, 'mumbai', 20, 'kolkatta', 30]

print("Your original list : ")
print(mylist)

print("Your list after processig : ")
print(onlynums(mylist))

