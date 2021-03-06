# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    result = 0.0
    it = 0
    for element in poly:
        result += poly[it]*x**it
        it += 1
    return result







# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    poly2 = poly[:]
    if len(poly2) == 1: return [0.0]
    it = 0
    for element in poly2:
        poly2[it] = float(poly2[it]*it)
        it += 1
    a = poly2.pop(0)
    return poly2




# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    it = 0
    x = x_0
    poly2 = poly[:]
    eva = evaluatePoly(poly, x_0)
    evader = None
    while abs(eva) > epsilon:
        eva = evaluatePoly(poly, x)
        poly2 = poly[:]
        evader = evaluatePoly(computeDeriv(poly2), x)
        x -= eva/evader
        it +=1
    return [x, it-1]



















    
