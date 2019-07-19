import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = DataFrame({'key1':['A']*2+['B']*3,
                    'key2':[2,2,2,3,3]})

# print(dframe)

# print(dframe.duplicated()) # Return TRUE if it is duplicated records, return FALSE if it is not duplicated

# print(dframe.drop_duplicates())  # return dataframe without duplicates

# print(dframe.drop_duplicates(['key1']))   # Only keep the records with distinct Key1 value.
                                            # Take the first instance, drop the later duplicates

print(dframe.drop_duplicates(['key1'],take_last=True))  # Take the last instance, drop the previous duplicates





