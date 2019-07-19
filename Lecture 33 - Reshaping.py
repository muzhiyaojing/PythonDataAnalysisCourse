import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe1 = DataFrame(np.arange(8).reshape(2,4),index=pd.Index(['LA','SF'],name='city')
                    , columns=pd.Index(['A','B','C','D'],name='letter'))

#print(dframe1)

# use pd.Index instead of Index to name the index

dframe_st = dframe1.stack()

#print(dframe1.unstack())

#print(dframe1.unstack('city'))
#print(dframe1.unstack('letter'))

#print(dframe_st)