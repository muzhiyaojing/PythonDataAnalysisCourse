import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series([1,2,3,4,1,2,3,4])
#ser1.replace(1,np.nan)   # replace all the 1 in the series with NAN value

# How to replace multiple values at once
ser2 = ser1.replace([1,4],[100,400])  # replace 1, 4 with 100, 400 respectively （分别的)

# Raplace with dictionary

ser3 = ser1.replace({4:np.nan})   # Question: Why is the data type change from int to float??????

print(ser3)
print(ser1)