def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    l1 = len(s1)
    l2 = len(s2)
    summ = []
    if l1 < l2:
        for i in range(0, l1):
            summ += s1[i]+s2[i]
        for i in range(l1, l2):
            summ += s2[i]
    elif l1 > l2:
        for i in range(0, l2):
            summ += s1[i]+s2[i]
        for i in range(l2, l1):
            summ += s1[i]
    elif l1 == l2:
        for i in range(0, l1):
            summ += s1[i]+s2[i]
    return "".join(summ)
