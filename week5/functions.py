
# accepts a string and calculate the number of upper case letters and lower case letters

def syntax(entry): 
    uCase = 0
    lCase = 0
    for elm in entry:
        if(elm.isupper()):
            uCase += 1
        else:
            lCase += 1
    print('There are ' + str(uCase) + ' uppercase letters and ' + str(lCase) + ' lowercase letters in the entry.') 
syntax('We Love Python!')