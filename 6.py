def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == b: return a
    elif max(a, b) - min(a, b) == 1: return 1
    return gcdRecur(max(a,b)-min(a,b),min(a,b))
