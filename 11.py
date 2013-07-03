def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum=0
    # Your Code Here
    if len(aDict) == 0: return 0
    elif (len(aDict) == 1) and (aDict[0]!=''): return 1
    elif len(aDict) > 1:
        for i in aDict:
            sum = sum + howMany(i)
    return sum
