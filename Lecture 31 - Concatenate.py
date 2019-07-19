import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr1 = np.arange(9).reshape(3,3)

arr2 = np.concatenate([arr1,arr1],axis = 1)  # axis = 1, 添加更多的column

arr3 = np.concatenate([arr1,arr1])  #不写axis， 则默认为添加更多的row

ser1 = Series([0,1,2],index=['T','U','V'])
ser2 = Series([3,4],index=['X','Y'])

#print(pd.concat([ser1,ser2],axis=1))

print_1 = pd.concat([ser1,ser2],keys=['cat1','cat2']) # key indicate which series that you used

dframe1 = DataFrame(np.random.randn(4,3),columns=['X','Y','Z'])
dframe2 = DataFrame(np.random.randn(3,3),columns=['Y','Q','X'])

print_2 = pd.concat([dframe1,dframe2])  # this index is recurrsive

print_3 = pd.concat([dframe1,dframe2],ignore_index=True)  # make the index in order

print(print_3)

