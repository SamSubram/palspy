# getnumlist version 1
'''
def onlynums(iList):
    olist=[]
    for iVal in iList:
        try:
            if int(iVal) >= 0 or int(iVal) < 0:
                olist.append(int(iVal))
        except:
            continue
    return olist

myList=['pal', 10, 20, 30, 'lion']
print("OrigList: ")
print(myList)
print("\n") 
print("Processed List: ")
print(onlynums(myList))
'''

#getnumlist version2
'''
def getNumLst(ilist):
    olist = [ temp if temp != -9999 else 0 for temp in ilist]
    return olist

mylist =[10, 20, 30, 'tep', 'mango', 50]
print(getNumLst(mylist))
'''

'''
# convert string in a list to 0s
def getNumLst(ilist):
    olist=[]
    for temp in ilist:
        try:
            if(int(temp) >= 0 or int(temp) < 0):
                olist.append(temp)
        except:
            olist.append(0)
    return olist

mylist =[10, 20, 30, 'tep', 'mango', 50]
print(getNumLst(mylist))
'''

# sum the values in a list
'''
def sumlist(iList):
    sumofval = 0.0
    
    for temp in iList:
        try:
            sumofval += float(temp)
        except:
            print("Not a float")
    return sumofval
'''

# average of undefined number of parameters
'''
def avNo(*args):
    return sum(args)/len(args)
'''
## str - convert to upper and sort and retun in a list

def strSort(*args):
    olist =[]
    for temp in args:
        olist.append(temp.upper())
    olist.sort()
    return olist

print(strSort("pala", "kal", "sam", "lio", "rio"))