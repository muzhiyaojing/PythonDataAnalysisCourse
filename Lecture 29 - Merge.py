import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe1 = DataFrame({'Key':['X','Z','Y','Z','X','X'],'data_set_1':np.arange(6)})

#print(dframe1)

dframe2 = DataFrame({'Key':['Q','Y','Z'], 'data_set_2':[1,2,3]})

#print(dframe2)

dframe3 = pd.merge(dframe2,dframe1)

dframe4 = pd.merge(dframe2,dframe1, on='Key')  #similar to SQL, join on condition

dframe5 = pd.merge(dframe2,dframe1, on ='Key', how='left')  # concept of left join, default is inner join
dframe6 =pd.merge(dframe1,dframe2, on ='Key',how='left')

dframe7 = pd.merge(dframe1,dframe2, on='Key', how='outer')  # concept of full join

dframe8 = DataFrame({'key':['X','X','X','Y','Z','Z'],'data_set_3':range(6)})

dframe9 = DataFrame({'key':['Y','Y','X','X','Z'],'data_set_4':range(5)})

dframe10 = pd.merge(dframe8, dframe9, on ='key')

df_left = DataFrame({'key1':['SF','SF','LA']
                        , 'key2':['one','two','three']
                        ,  'left_data':[10,20,30]})
df_right = DataFrame({'key1':['SF','SF','LA','LA'],
                      'key2':['one','one','one','two']
                      ,'right_data':[40,50,60,70]})

print(df_left)

print(df_right)

df_merge1 = pd.merge(df_left, df_right, on =['key1','key2'], how='outer') # join on multiple conditions
df_merge2 = pd.merge(df_left,df_right,on='key1', suffixes = ('_lefty','_righty')) #customize suffix
#print(df_merge1)
print(df_merge2)


