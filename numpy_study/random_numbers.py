import numpy as np

rng = np.random.default_rng()

print(rng.integers(1, 7)) #random number 1 - 6

print(rng.integers(low=1, high=7, size=3)) 
#sample output 1D [6 5 4]

print(rng.integers(low=1, high=7, size=(3, 2))) 
#sample out 2D [[4 5]
#               [6 1]
#               [5 1]]