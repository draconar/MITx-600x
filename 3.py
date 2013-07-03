def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    if exp == 0:
        result = int(1)
    else:
        while exp > o:
            result = base*result
            exp -= 1
    return result
