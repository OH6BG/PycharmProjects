from math import erf, sqrt
import numpy as np

"""
A small script to generate positive and negative Z tables
2019 Jari Perkiömäki OH6BG
"""

def phi(z):
    return (1.0 + erf(z / sqrt(2.0))) / 2.0


# Positive Z table
print(" " * 4, end='')
for j in np.arange(0.00, 0.1, 0.01):
    print("%9.2f" % j, end='')
print()

for i in np.arange(0.0, 3.7, 0.1):
    print("%4.1f" % i, end='')
    for j in np.arange(0.00, 0.1, 0.01):
        print("%9.4f" % phi(i+j), end='')
    print()

# Negative Z table
print()
print(" " * 4, end='')
for j in np.arange(0.00, 0.1, 0.01):
    print("%9.2f" % j, end='')
print()

for i in np.arange(-3.6, 0.1, 0.1):

    if i < 0:
        print("%4.1f" % i, end='')
    else:
        print("%4.1f" % -i, end='')

    for j in np.arange(0.00, 0.1, 0.01):
        print("%9.4f" % phi(i-j), end='')
    print()
