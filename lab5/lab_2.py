'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
Cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
    ])

# P(Cancer|Positive results on both tests).
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), Cancer).show_approx())
# P(Cancer|test1 positive, test2 negative).
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), Cancer).show_approx())



"""
A)
Handwork:
P(C | T1 ^ T2) = alpha <P(T1 | C) * P(T2 | C) * P(C), P(T1 | -C) * P(T2 | -C) * P(-C))
    = alpha <0.9 * 0.9 * 0.01,  0.2 * 0.2 * 0.99>
    = alpha <0.0081, 0.0396>
    = <0.17, 0.83>
   
B)
Handwork:
P(C | T1 ^ -T2) = alpha <P(T1 | C) * P(-T2 | C) * P(C), P(T1 | -C) * P(-T2 | -C) * P(-C)
    = alpha <0.9 * 0.1 * 0.01, 0.2 * (1 - 0.2) * 0.99)
    = alpha <0.0009, 0.1584>
    = <0.00565, 0.994>
    
"""

"""
The results do make sense in a way that one fails a test being negative,
the chance of having cancer extremely decreases.
"""
