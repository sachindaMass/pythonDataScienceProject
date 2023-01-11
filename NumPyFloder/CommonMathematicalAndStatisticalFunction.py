import numpy as np

arr = np.array([[4, 3, 2], [10, 1, 0], [5, 8, 24]])
print(arr)
# [[ 4  3  2]
#  [10  1  0]
#  [ 5  8 24]]

print(np.amin(arr))
# 0

print(np.amin(arr, axis=0))  # 0 means vertical
# [4 1 0]

print(np.amin(arr, axis=1))  # 1 means horizontal
# [2 0 5]

print(np.max(arr))
# 24

print(np.amax(arr, axis=0))  # 0 means vertical
# [10  8 24]

print(np.amax(arr, axis=1))  # 1 means horizontal
# [ 4 10 24]

print(np.median(arr))
# 4.0

print(np.mean(arr))
# 6.333333333333333

print(np.std(arr))  # the standard deviation
# 6.944222218666553

print(np.var(arr))  # variance
# 48.22222222222222

print(np.percentile(arr, 50))
# 4.0

deg = np.array([0,30,45,60,90])

print(np.sin((deg*np.pi/180)))
# [0.         0.5        0.70710678 0.8660254  1.        ]

print(np.cos((deg*np.pi/180)))
# [1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
#  6.12323400e-17]

print(np.tan((deg*np.pi/180)))
# [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
#  1.63312394e+16]

# There can be use arcsin, arccos and arctan.

arr = np.array([0.1,0.8,-2.2,-9.87])

print(np.floor(arr)) # for the rounded values
# [  0.   0.  -3. -10.]

print(np.ceil(arr)) # for the ceil value
# [ 1.  1. -2. -9.]