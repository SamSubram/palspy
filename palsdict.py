import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictMatcher(inWord):
    inWord = inWord.lower()

    if inWord in data:
        return data[inWord]

    elif inWord.title() in data:
        return data[inWord.title()]

    elif inWord.upper() in data:
        return data[inWord.upper()]
    
    elif len(get_close_matches(inWord, data.keys())) > 0:
        yn = input("Did you mean %s. Please enter Y for yes and N for No" %get_close_matches(inWord, data.keys())[0])
        if(yn == 'Y'):
            return data[get_close_matches(inWord, data.keys())[0]]
        else:
            return "Word does not exist."
    else:
        return "Please recheck. This word does not exist."

word = input("Welcome to Pals Dictionary. Enter your word:")
outStr = dictMatcher(word)

if type(outStr) == list:
    for item in outStr:
        print(item)
else:
    print(outStr)

 

