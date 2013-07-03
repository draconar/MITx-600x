def isPrime(n): 
    try: 
        if type(n)!=int: 
            raise TypeError 
        elif n<=0: 
            raise ValueError 
    except TypeError: 
        raise
    except ValueError: 
        raise
    else:
        for d in range(2,n/2+1):
            if n%d==0:
                return False
    return True
