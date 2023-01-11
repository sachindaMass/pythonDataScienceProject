import pandas as pd

s = pd.Series([x for x in range(1, 11)])

print(s)
# 0     1
# 1     2
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9    10
# dtype: int64

print(s.iloc[0])  # Specify the index
# 1

print(s.iloc[5])  # Specify the index
# 6

print(s.iat[0])  # Specify the index, same as iloc
# 1

print(s.iloc[5])  # Specify the index, same as iloc
#  6

# ------------------------------- Slicing a Series --------------------------------------------- #

print(s[5:9])
# 5    6
# 6    7
# 7    8
# 8    9
# dtype: int64

print(s[-4:-1])  # negative value can be access
# 6    7
# 7    8
# 8    9
# dtype: int64

# ------------------------------------------------------------------------------------------------------- #
# -------------------------------- check conditions ----------------------------------------------------- #

print(s.where(s % 2 == 0))  # specify the condition and return true and false
# 0     NaN
# 1     2.0
# 2     NaN
# 3     4.0
# 4     NaN
# 5     6.0
# 6     NaN
# 7     8.0
# 8     NaN
# 9    10.0
# dtype: float64

print(s.where(s % 2 == 0, 'Odd Number'))
# 0    Odd Number
# 1             2
# 2    Odd Number
# 3             4
# 4    Odd Number
# 5             6
# 6    Odd Number
# 7             8
# 8    Odd Number
# 9            10
# dtype: object

print(s.where(s % 2 == 0, s ** 2))  # check two conditions
# 0     1
# 1     2
# 2     9
# 3     4
# 4    25
# 5     6
# 6    49
# 7     8
# 8    81
# 9    10
# dtype: int64

s.where(s % 2 == 0, inplace=True)

print(s.dropna())
# 1     2.0
# 3     4.0
# 5     6.0
# 7     8.0
# 9    10.0
# dtype: float64

print(s.fillna('Filled value'))
# 0    Filled value
# 1             2.0
# 2    Filled value
# 3             4.0
# 4    Filled value
# 5             6.0
# 6    Filled value
# 7             8.0
# 8    Filled value
# 9            10.0
# dtype: object