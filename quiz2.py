def probTest(limit):
    p = 1.0/6.0
    m = 1.0
    while limit <= p:
        m += 1.0
        p = ((5.0)**(m-1))/6.0**m
    return int(m)

