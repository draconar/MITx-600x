def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    elif exp%2==0:
        return (recurPowerNew(recurPowerNew(base, 2), exp/2))
    return base*recurPowerNew(base, exp-1)
