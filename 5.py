def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    for divis in range (min(a,b), 0, -1):
        if a%divis==0 and b%divis==0: return divis
