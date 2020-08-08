def findCharInFile(schar, fpath):
    numOccur=0
    with open(fpath) as myfile:
        contents = myfile.read()
    for tempStr in contents:
        if(schar == tempStr):
            numOccur +=1
    return numOccur


searchChar='c'
filePath="Cities.txt"
print(filePath + " has the character ["+searchChar+"]: " + str(findCharInFile(searchChar,filePath)) + " times")