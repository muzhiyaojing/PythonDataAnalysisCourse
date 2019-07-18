import numpy as np
import pandas as pd
from pandas import Series

dframe = pd.DataFrame(np.arange(16).reshape(4,4))

blender = np.random.permutation(4)  #permutation: 排列

"""
numpy.random.permutaiton: Randomly permute(排列) a sequence, 
or return a permuted range. 
If x is a multi-dimensional array, it is only shuffled along its first index
i.e. array.shape = (3,4). Then this is a multi-dimensional array, it will only 
shuffle on the row level. It won't change the column order.

How to use it?

np.random.permutation(10) --- similar to arange. but numbers are in random order

np.random.permutation([1,4,9,12,15])

"""
"""
If the output of blender is array([1,2,0,3])
Then dframe.take(blender) means order the dframe using order 
[1,2,0,3] -- index order
"""
dframe.take(blender)

# Do the permutation with replacement.

box=np.array([1,2,3])
shaker = np.random.randint(0,len(box),size=10)
# 0 is the minimum number, len(box) is the maximum number
# size -- how many numbers do we want to put into the shaker.

hand_grabs = dframe.take(shaker)
print(hand_grabs)