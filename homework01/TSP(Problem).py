"""
This TSP Problem implements local search algorihtm to find solution, through using AIMA-Python.


Taek Soo Nam(tn32)
23rd Feb 2019

"""


from tools.aima.search import Problem, hill_climbing, simulated_annealing, exp_schedule
import random


class TSP(Problem):


    def __init__(self, initial, distances, num_cities):
        self.initial = initial
        self.distances = distances
        self.num_cities = num_cities

    def actions(self, state):
        swap = []
        for i in range (5):
            pairs = [random.sample(range(1, len(state) -1), 2)]
        swap.append (pairs)
        return swap

    def result(self, state, move):
        new_state = state[:]
        pairs1 = state[move[0][0]]
        pairs2 = state[move[0][1]]
        new_state[move[0][0]] = pairs1
        new_state[move[0][1]] = pairs2
        return new_state

    def value(self, state):
        distance = 0
        for i in range(len(state) - 1):
            lst = [state[i], state[i+1]]
            lst.sort()
            distance += self.distances[tuple(lst)]
        return -1 * distance







"""
State: A complete city circuit, e.g., [0, 1, 2, 3, 0] (note that this starts and stops in the same, constant city)


Distances: A dictionary city-pair-distances, e.g., {(1,2): 1.5, (2,3): 2.3, ...}

actions(state) returns a list of pairs of cities to swap in the current state, e.g., [[1,2], [3,5], ...]

result(state, action) returns the new state resulting from applying the given action to the given state. 
This must be a pure function.

value(state) returns the sum of the distances between the cites in the given state, negated in order to reflect value.

"""

if __name__ == '__main__':
    num_cities = 5
    path = ['1', '2', '3', '4', '5', '6', '1']
    distances = {('1','2'): 1, ('1','3'): 2, ('1','4'): 3, ('1','5'): 4, ('1','6'): 5,
                 ('2','3'): 1, ('2','4'): 2, ('2','5'): 3, ('2','6'): 4,
                 ('3','4'): 1, ('3','5'): 2, ('3','6'): 3,
                 ('4','5'): 1, ('4','6'): 2,
                 ('5','6'): 1}

    print('Start: ' + str(path))


    p = TSP(initial=path, distances=distances, num_cities=num_cities)
    print('Value:    ' + str(p.value(path)))

    #hill_climbing solution
    hill_solution = hill_climbing(p)
    print('Hill-climbing:')
    print('\tSolution: ' + str(hill_solution))
    print('\tValue:    ' + str(p.value(hill_solution)))

    #simulated annealing solution
    annealing_solution = simulated_annealing(p,
        exp_schedule(k=20, lam=0.005, limit=10000)
    )
    print('Simulated annealing:')
    print('\tSolution: ' + str(annealing_solution))
    print('\tValue:    ' + str(p.value(annealing_solution)))
