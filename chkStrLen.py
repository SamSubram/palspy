def chkStr(myStr):
    if(len(myStr) > 8):
        return True
    else:
        return False
        
    
myStr = 'enchante!'
print(myStr + "  Enter your string")
try:
    myStr = input()
    if chkStr(myStr):
        print("Longer")
    else:
        print("shorter")
        
except:
    print("Invalid string entered")
    