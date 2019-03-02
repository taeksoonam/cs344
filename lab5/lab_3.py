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
Happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])
# A

# P(Raise|Sunny).
print(enumeration_ask('Raise', dict(Sunny=T), Happy).show_approx())
# P(Raise|happy ^ Sunny).
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), Happy).show_approx())


"""
Handwork:
i)
    P(Raise | Sunny) = <P(Raise | Sunny), P(-Raise | Sunny)>
    = alpha * <0.01 * 0.7, 0.99 * 0.7>
    = alpha * <0.007, 0.693>
    = <0.01, 0.99>
    Since Raise and Sunny are not both dependent to teach other, the result makes sense, which is 0.01.
ii)
   P(Raise | Happy ^ Sunny)
    = alpha * P(Raise, Happy, Sunny)
    = alpha * P(Raise) * P(Sunny) * P(Happy | Raise, Sunny)
    = alpha * <0.01 * 1.0 * 0.7, 0.99 * 0.7 * 0.7>
    = alpha * <0.007, 0.4851>
    = <0.0142, 0.986>
    This time, the probability of sunny is related to happiness and raise.  

"""

# B

# P(Raise|happy).
print(enumeration_ask('Raise', dict(Happy=T), Happy).show_approx())
# P(Raise|happy ^ -Sunny).
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), Happy).show_approx())

"""
These results above do make sense because the probability of being happy assuming because of raise should be low
due to the nature of a chance of raise happening is low.
Moreover, the probability of a person being happy without the weather being sunny should be low,
since the probability of a person being happy is high almost when the weather is sunny.
"""

