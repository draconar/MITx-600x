def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    ka = 6
    kb = 9
    kc = 20
    na = n/ka
    nb = n/kb
    nc = n/kc
    a = 0
    b = 0
    c = 0
    if (n == ka) or (n == kb) or (n == kc): return True    
    elif n < ka: return False
    else:
        for c in range(nc+1):
            for b in range(nb+1):
                for a in range(na+1):
                    if ka*a+kb*b+kc*c == n: return True
    return False
