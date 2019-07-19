# Summary : There are two ways to rename the index and column name
# option 1: use 'MAP' method
# option 2: use 'rename' method
# You can pass argus(function, dictionary) to the rename method to update index name and column name
# 'inplace = True' will make the changes to be permanent.


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.DataFrame(np.arange(12).reshape(3,4),
                      index = ['NY','LA','SF'],
                      columns = ['A','B','C','D'])

dframe.index = dframe.index.map(str.lower)

# print(dframe)

# print(dframe.rename(index=str.title, columns = str.lower))

dframe.rename(index = {'ny':'New York'}, columns={'A':'ALPHA'}, inplace=True)

# 'inplace = True' means that the change is permanent

print(dframe)