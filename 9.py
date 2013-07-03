def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr<='': return False
    elif aStr==char: return True
    elif (len(aStr)==1 and aStr!=char): return False
    elif aStr[len(aStr)/2]==char: return True
    elif aStr[len(aStr)/2]<char: return isIn(char, aStr[len(aStr)/2:])
    elif aStr[len(aStr)/2]>char: return isIn(char, aStr[:len(aStr)/2])
