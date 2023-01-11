import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# -------------------------------------- Indexing Array ------------------------------------------------- #

print(array_1d[0])  # print first element
# 1

print(array_1d[1])  # print second element
# 2

print(array_1d[-4])  # print 4th element
# 3

print(array_2d)  # print array_2nd
# [[1 2 3]
#  [4 5 6]]

print(array_2d[0, 0])  # print 2nd array 1st element
#  1

print(array_2d[0, 1])  # print 2nd array 2nd element
# 2

print(array_2d[1, -1])  # print 2nd array last element
# 6

print(array_3d)  # print array_3d
# [[[ 1  2  3]
#   [ 4  5  6]]
#  [[ 7  8  9]
#   [10 11 12]]]

print(array_3d[0, 1, 2])  # print 3rd element 2nd row of the 1st array
# 6

print(array_3d[1, -1, -1])  # print last element
# 12

# ------------------------------------------------------------------------------------------------------------ #

# ------------------------------------ Slicing --------------------------------------------------------------- #

print(array_1d[1:])  # print 2nd elements to towards
# [2 3 4 5 6]

print(array_1d[3:5])  # print 4 th to 5th elements
# [4 5]

print(array_1d[-3: -1])  # need to find the definition
# [4 5]

print(array_2d[1, 1:])  # print 2nd array 2nd elements towards
# [5 6]

print(array_2d[-2:-3:-1])  # need to find the definition
# [[1 2 3]]

print(array_3d[0, 1:, 1:])  # 1st array 2nd row 1st element to 1st element
# [[5 6]]
