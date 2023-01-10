import numpy as np

arr = np.array([[4, 3, 2], [10, 1, 0], [5, 8, 24]])
print(arr)
# [[ 4  3  2]
#  [10  1  0]
#  [ 5  8 24]]

print(np.amin(arr))
# 0

print (np.amin(arr,axis=0)) # 0 means vertical
# [4 1 0]

print (np.amin(arr,axis=1)) # 1 means horizontal
# [2 0 5]

print(np.max(arr))
# 24

print(np.amax(arr,axis=0)) # 0 means vertical
# [10  8 24]

print(np.amax(arr,axis=1)) # 1 means horizontal
# [ 4 10 24]

print(np.median(arr))
# 4.0

print(np.mean (arr))
# 6.333333333333333

print(np.std (arr)) #the standard deviation
# 6.944222218666553

print(np.var(arr)) # variance
# 48.22222222222222

print(np.percentile(arr,50))
# 4.0