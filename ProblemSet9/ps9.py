# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    delays = [300,150,75,0]
    results = [[],[],[],[]]
    for place in range(0, 4):
        for trial in range(numTrials):
            viruses = []
            for num in range(100):
                viruses.append(ResistantVirus(0.1,0.05, {'guttagonol': False}, 0.005))
            patient = TreatedPatient(viruses, 1000)
            for delay in range(delays[place]):
                patient.update()
            patient.addPrescription("guttagonol")  
            for l in range(150):
                patient.update()
            results[place].append(patient.getTotalPop())
    pylab.hist(results[0])
    pylab.hist(results[1])
    pylab.hist(results[2])
    pylab.hist(results[3])
    pylab.show()
    for x in range(0, 10):






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
