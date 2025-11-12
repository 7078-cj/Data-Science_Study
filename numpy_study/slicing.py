import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

#array[start:end:step]

#first row
print(array[0])
#[1 2 3 4]

#getting the 1st three
print(array[0:3])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]


#getting the 1st three w/ step
print(array[1:4:2])
# [[ 5  6  7  8]
#  [13 14 15 16]]

#selecting rows and accessing columns
print(array[:,0])
#[ 1  5  9 13]