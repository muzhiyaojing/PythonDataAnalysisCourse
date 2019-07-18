import numpy as np
import pandas as pd
from pandas import Series, DataFrame

np.random.seed(12345)   # How to use np.random.seed

dframe = DataFrame(np.random.randn(1000,4))

# print(dframe.head())     # head() returns the first 5 columns
# print(dframe.tail())     # tail() returns the last 5 columns
# print(dframe.describe())

col=dframe[0]
# print(col[np.abs(col)>3])  # return values in the first column that abs are greater than 3
# print(dframe[(np.abs(dframe)>3).any(1)]) # returns values in the entire dataframe that abs are greater than 3.
                                         # what is the meaning of any????
# anywhere in the dataframe where the absolute value is greater than 3
# set that value to the sign of the that value, which either be negative 1 or 1
# set the value equal to that sign times 3
# numpy.sign -- returns -1 if x<0, 0 if x==0, 1 if x>0

dframe[np.abs(dframe)>3] = np.sign(dframe)*3
print(dframe.describe())