# import math
# import NumPy
import numpy as np

# a = 16
# print(math.sqrt(a))

# first Numpy array
first_numpy_array = np.array([1, 2, 3, 4])  # Regular array: Brackets
print(first_numpy_array)  # [1,2,3,4]

# array with zeros
array_with_zeros = np.zeros((3, 3))  # Zero array: Parantheses, 3 rows and 3 columns
print(array_with_zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# array with ones
array_with_ones = np.ones((3, 3))
print(array_with_ones)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# array with empty
array_with_empty = np.empty((2, 3))  # 2 rows and 3 columns
print(array_with_empty)
# [[9.10016855e+276 4.19338058e+228 2.46635480e-154]
#  [1.05849799e+200 1.95848521e-152 1.69592895e-152]]

# array with arrange method
np_arange = np.arange(12)  # Range of the array, one D array
print(np_arange)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# reshape ,method to change / create array
np_reshape = np_arange.reshape(3, 4)  # 3 rows and 4 columns
print(np_reshape)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# linspace for linearly (equal) spaced data elements
np_line_space = np.linspace(1, 6, 5)  # first element 1, last element 6, total nu of equidistant elements 5
print(np_line_space)
# [1.   2.25 3.5  4.75 6.  ]

# one Dimenisional array
oneD_array = np.arange(15)  # 15 elements array
print(oneD_array)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# Two dimensional array
twoD_array = oneD_array.reshape(3, 5)
print(twoD_array)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

# Three-dimensional array
threeD_array = np.arange(27).reshape(3, 3, 3)
print(threeD_array)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]

# -------------------------------------------------------------------------------------------------------------------- #
# ndarray attributes
# ndarry.ndim - the number of axes (dimensions ) ot the array
# ndarry.shape - Tuple of integers that gives the size of the array in each dimension.
# For an m n matrix, shape is (n,m). the length of the shpe tuple is the number of axes, ndim.
# ndarry.size - the total number of elements of the array is equal to the product of the elements of the shape.
# ndarry.dtype - An object that describes the type of elements in the array. (numpy.int32, numpy.int16, numpy.float64).
# ndarray.itemsize: Size  in bytes if each element of the array.if the item size is 64/8 = 8. for complex 32, the
# itemsize is 32/8 = 4.(Denoted by ndarry.dtype.itemsize ).
# ndarray.data - The buffer contains the actual elements of the array. However, for accessing the elements of the array,
# use indexing and not ndarray.data.

# -------------------------------------------------------------------------------------------------------------------- #

zeroDimensionArray = np.array(24)
print(zeroDimensionArray)
# 24

oneDimensionArray = np.array([1, 2, 3, 4])
print(oneDimensionArray)
# [1 2 3 4]

twoDimensionArray = np.array([[1, 2, 3], [1, 1, 1]])
print(twoDimensionArray)
# [[1 2 3]
# [1 1 1]]

threeDimensionArray = np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]]])
print(threeDimensionArray)
# [[[1 1 1]
#   [2 2 2]
#   [3 3 3]]]

print(threeDimensionArray.shape)
# (1, 3, 3)

print(threeDimensionArray.ndim)
# 3

numpy_arr = np.array([x for x in range(1, 10)])
print(numpy_arr)
# [1 2 3 4 5 6 7 8 9]

numpy_arr_reshape_to_2D = numpy_arr.reshape(3, 3)
print(numpy_arr_reshape_to_2D)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

numpy_arr = np.array([x for x in range(1, 13)])
print(numpy_arr)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

numpy_arr_reshape_to_3D = numpy_arr.reshape(2, 2, 3)  # - size 12
print(numpy_arr_reshape_to_3D)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print(numpy_arr_reshape_to_3D.reshape(3, 2, 2))  # - size 12
# [[[ 1  2]
#   [ 3  4]]
#
#  [[ 5  6]
#   [ 7  8]]
#
#  [[ 9 10]
#   [11 12]]]

# print(numpy_arr_reshape_to_3D.reshape(3,2,3)) - size 18
# ValueError: cannot reshape array of size 12 into shape (3,2,3)

print(numpy_arr_reshape_to_3D.reshape(2, 2, -1))
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

print(numpy_arr_reshape_to_3D.reshape(3, 2, 2))
# [[[ 1  2]
#   [ 3  4]]
#
#  [[ 5  6]
#   [ 7  8]]
#
#  [[ 9 10]
#   [11 12]]]

print(numpy_arr_reshape_to_3D.reshape(-1))
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

