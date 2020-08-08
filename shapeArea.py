def shapeSqArea(side):
    return side*side

def shapeReArea(length, breadth):
    return length * breadth
    
print ( "Enter the dimensions of your shape")

try:
    side = input()
    print("area you done?")
    followRes = str(input())
    if(followRes == 'yes'):
        print("Area of square with the side " + str(side) + "is = " + str(shapeSqArea(side)))
    else:
        print("Enter the side 2")
        try:
            side2 = input()
            print("Area of rectangle is " + str(shapeReArea(side, side2)))
            
        except:
            print("You did not enter a valid value for side 2")

except:
    print("Invalid Input")