import pandas as pd
from pandas import Series, DataFrame

import numpy as np

df_left = DataFrame({'key':['X','Y','Z','X','Y'],'data':range(5)})

df_right = DataFrame({'group_data':[10,20]},index=['X','Y'])

df_merge = pd.merge(df_left, df_right, left_on='key',right_index=True) #左边的dataset用key进行join，

#print(df_merge)

df_left_hr = DataFrame({'key1':['SF','SF','SF','LA','LA']
                            , 'key2':[10,20,30,20,30]
                            , 'data_set':np.arange(5)})


df_right_hr = DataFrame(np.arange(10).reshape(5,2)
                        , index = [['LA','LA','SF','SF','SF'],
                                    [20,10,10,10,20]], columns=['col_1','col_2'])

df_merge1 = pd.merge(df_left_hr, df_right_hr, left_on=['key1','key2'],right_index=True)

df_left.join  # Research on the use of join.