import numpy as np

x = np.array([i for i in range(10)])

print(x)
# [0 1 2 3 4 5 6 7 8 9]

print(np.where(x % 2 == 0, 'Even', 'Odd'))
# ['Even' 'Odd' 'Even' 'Odd' 'Even' 'Odd' 'Even' 'Odd' 'Even' 'Odd']

condList = [x < 5, x > 5]
choiceList = [x ** 2, x ** 3]

npNewList = np.select(condList, choiceList, default=x) # parsing value to npNewList
print(npNewList)
# [  0   1   4   9  16   5 216 343 512 729]
