"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange, random
import math
import time


class SineVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.0001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x*math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.

    Hill_dict = {}
    Annealing_dict = {}

    for x in range(20):
        maximum = 30
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=3.0)

    # Solve the problem using hill-climbing.

        start1 = time.time()
        hill_solution = hill_climbing(p)
        Hill_dict[p.value(hill_solution)] = hill_solution
        end1 = time.time()

        # Solve the problem using simulated annealing.
        start2 = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        Annealing_dict[p.value(annealing_solution)] = annealing_solution
        end2 = time.time()

    hill_maxValue = max(Hill_dict.keys())
    annealing_maxValue = max(Annealing_dict.keys())

    print('Hill-climbing solution       x: ' + str(Hill_dict.get(hill_maxValue))
          + '\tvalue: ' + str(hill_maxValue)
          + '\n' + str(end1 - start1) + '\n')

    print('Simulated annealing solution x: ' + str(Annealing_dict.get(annealing_maxValue))
          + '\tvalue: ' + str(annealing_maxValue)
          + '\n' + str(end2 - start2))
