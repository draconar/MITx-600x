def test(numTrials=1000):
    import random
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    # Your Code Here
    africa = []
    other = []
    maxrank = []
    end = []
    q = 0
    for i in range(0, 250):
        africa.append(random.random()*100)
    for i in range(0, 750):
        other.append(random.random()*100)
    #bubble sort for list of other students
    Flag = True
    while Flag:
        Flag = False
        for i in range(len(other)-1):
            if other[i] < other[i+1]:
                temp = other[i+1]
                other[i+1] = other[i]
                other[i] = temp
                Flag = True
    #end of other sort
    #bubble sort for list of africa students
    Flag = True
    while Flag:
        Flag = False
        for i in range(len(africa)-1):
            if africa[i] < africa[i+1]:
                temp = africa[i+1]
                africa[i+1] = africa[i]
                africa[i] = temp
                Flag = True
    #end of other sort
    maxrank = other[:100]
    maxafrica = africa[:100]
    while len(end)<=100:
        for i in range(100):
