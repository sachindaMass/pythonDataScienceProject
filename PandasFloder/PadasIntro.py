# pandas is and open-source library, which is a simple and easy to us tool for data analysis.
# Two mager factors - series and dataFrames
# A Pandas series is a one-dimensional ndarry with axis labels
# Pandas dataFrames is a two-dimensional heterogeneous tabular data similar to spread-sheet,with data as rows
# and columns.
# Panel, a three-dimensional data representation - Datetime, timeDelta, Textual Data.
# Read and write data, Describe data, Grab subset of the main dataset, Convert to different types of data, Group,
# Wrangle oe mug data, merge and sort data, Find missing values, Drop or exclude values.

# ---------------------------------- Series --------------------------------------------- #

# One dimesinonal ndarray with access label. where you can access the element using labels.

import pandas as pd

l = [x for x in range(5)]
s = pd.Series(l);

print(s)
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# dtype: int64

print(s[3])
#  3

s = pd.Series(l, index=['a', 'b', 'c', 'd', 'e'])  # manually add index

print(s)
# a    0
# b    1
# c    2
# d    3
# e    4
# dtype: int64

print(s['e'])
# 4

s = pd.Series(l, index=['a', 'b', 'c', 'd', 'd'])

print(s['d'])
# d    3
# d    4

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

s = pd.Series(data)

print(s)
# a    1
# b    2
# c    3
# d    4
# dtype: int64

s = pd.Series(data, index=['a', 'b'])

print(s)
# a    1
# b    2
# dtype: int64

s = pd.Series(data, index=['a', 'b', 'c', 'f'])

print(s)
# a    1.0
# b    2.0
# c    3.0
# f    NaN - No value in relevant index
# dtype: float64
