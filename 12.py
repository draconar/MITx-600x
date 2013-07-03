def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum = 0
    for key in aDict:
              elLen = len(aDict[key])
              if (elLen > 0):
                  sum += elLen 
              if (aDict[key] == {}):
                return 0
    return sum


def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum = 0
    for key in aDict:
        if len(aDict[key]) > 0: sum += len(aDict[key]) 
        elif aDict[key] == {}: return 0
    return sum
