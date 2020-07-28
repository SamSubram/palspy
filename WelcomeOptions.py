def LongWelcome():
    print('Please enter you first Name')
    firstName = input()
    print('Last Name as well, Please!')
    LastName = input()
    print('Welcome to PyWonder ', firstName , LastName)

def ShortWelcome():
    print('What is your name?')
    fName = input()
    print('Nice meeting you! ' + fName + ' Have a great day!')

print('Hello, This PyWonder!')
print('Select option to play: I have lot of time:  1, I am in a hurry: 2')

SelectedOption = input()

if SelectedOption == '1':
    LongWelcome()
elif SelectedOption == '2':
    ShortWelcome()
else:
    print('Incorrect option. Thank you! Bye')

