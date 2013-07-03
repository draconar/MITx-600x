import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''    
    all = 0.0
    for trial in range(numTrials):
        pot = ['r','r','r','g','g','g']
        d1 = pot.pop(pot.index(random.choice(pot)))
        d2 = pot.pop(pot.index(random.choice(pot)))
        d3 = pot.pop(pot.index(random.choice(pot)))
        if (d1 == 'r' and d2 == 'r' and d3 == 'r') or (d1 == 'g' and d2 == 'g' and d3 == 'g'):
            all += 1.0
    return all/numTrials
