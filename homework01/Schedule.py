"""
Course Scheduling program for CS Department at Calvin College
Taek Soo Nam (tn32)
23rd Feb 2019
"""

from tools.aima.csp import min_conflicts, CSP, parse_neighbors, backtracking_search, min_conflicts,  AC3
from search import depth_first_graph_search

def schedule():
    """
    """
    faculty = ['Joel Adams', 'Patrick Bailey', 'Harry Plantinga', 'Derek Shuurman', 'Keith Vanderlinden']
    class_time = ['mwf900', 'mwf1030', 'mwf1330', 'tth1030', 'tth1800']
    classroom = ['sb382', 'nh253']
    classes = ['cs108', 'cs112', 'cs212', 'cs342', 'cs374', 'cs344', 'is171']
    domain = {}
    assigned_course = {'cs108': 'Derek Shuurman', 'cs112': 'Joel Adams', 'cs212': 'Harry Plantinga',
                  'cs374': 'Joel Adams', 'cs344': 'Keith Vanderlinden', 'is171': 'Patrick Bailey',
                  'cs342': 'Patrick Bailey'}

    # Parsing neighbors: each two courses.
    neighbors = parse_neighbors(""" cs108: cs112; cs112: cs212; cs212: cs342; 
                                cs342: cs374; cs374: cs344; cs344: is171; is171: cs108""",
                                classes)

    for size in classes:
        for A in size:
            for B in size:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    for var in classes:
        domain[var] = []
        for instructors in faculty:
            for time_slot in class_time:
                for room_num in classroom:
                    domain[var].append([instructors, time_slot, room_num])

    def constraints(A, a, B, b, recurse=0):
        """
        Does not allow overlapping class or time
        Does not allow overlapping time or professors
        A: Variable 1
        B: Variable 2
        a: attribute list of Variable 1
        b: attribute list of Variable 2
        [0]: Professor
        [1]: Class time
        [2]: Classroom
        """
        # check inst assignments:
        if assigned_course[A] != a[0] and assigned_course[B] != b[0]:
            return False

        # check same room and same time
        if a[1] == b[1] and a[2] == b[2]:
            return False

        # check same inst and same time
        if a[1] == b[1] and a[0] == b[0]:
            return False

        return True

    return CSP(classes, domain, neighbors, constraints)

#In order to define class problems, I took out classes
classes = ['cs108', 'cs112', 'cs212', 'cs342', 'cs374', 'cs344', 'is371']

def print_solution(solution):
    """A CSP solution printer copied from csp.py."""
    for h in classes:
        print('For class: \t' + h)
        for (var, val) in solution.items():
            if var == h: print('\t\t'+'\n\t\t'.join(val))


p = schedule()
#different algorithms
# solution = depth_first_graph_search(p)
# solution = AC3(p)
# solution = backtracking_search(p)
solution = min_conflicts(p, max_steps=1000)
print_solution(solution)
