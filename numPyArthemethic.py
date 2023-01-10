import numpy as np

a = np.array([[1, 2, 1], [2, 2, 3]]) # two-dimensional array
b = np.array([3, 4, 5]) # one-dimensional

print(a)
# [[1 2 1]
#  [2 2 3]]
print (b)
# [3 4 5]

additionOfTwoArrays = np.add(a, b)
print(additionOfTwoArrays)
# [[4 6 6]
#  [5 6 8]]

print(np.subtract(b, a))
# [[2 2 4]
#  [1 2 2]]

print(np.multiply(a, b))
# [[ 3  8  5]
#  [ 6  8 15]]

print(np.divide(a,b))
# [[0.33333333 0.5        0.2       ]
#  [0.66666667 0.5        0.6       ]]

print(np.power(a, 2))
# [[1 4 1]
#  [4 4 9]]

print(np.power(a, b))
# [[  1  16   1]
#  [  8  16 243]]