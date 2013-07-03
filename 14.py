def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict) == 0 : return None
    big = None
    keylist = aDict.keys()
    iter = 0
    k = None
    for key in aDict:
        if len(aDict[key]) >= big:
           big = len(aDict[key])
           k = keylist[iter]
        iter += 1
    else: return k
