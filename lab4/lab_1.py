'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from tools.aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|catch = T)
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)

print(PC.show_approx())

'''
4.1b
I have done P(cavity^catch)/P(catch) = 0.108/0.34 = 0.529.
This answer validates the answer computed through coding.
'''

#4.1c
# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P2 = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
P2[T, T] = 0.25; P2[T, F] = 0.25
P2[F, T] = 0.25; P2[F, F] = 0.25


# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC2 = enumerate_joint_ask('Coin2', {'Coin1': T}, P2)
print(PC.show_approx())


'''
Yes. I have done P(Coin2|Coin1=heads) and the result was 0.5
'''

'''
Full join is generally not used in probabilistic systems, 
because it is too inefficient to draw out and calculate all the probabilities out.
Users would just use simpler ways to compute probabilities.
'''

