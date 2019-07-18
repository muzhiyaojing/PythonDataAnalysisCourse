import pandas as pd
import numpy as np
from pandas import Series, DataFrame

years = [1990,1991,1992,2008,2012, 2015,1987,1969,2013,2008,1999]

#### Specify the bin list
decade_bins = [1960,1970,1980,1990,2000,2010,2020]

decade_cat=pd.cut(years,decade_bins)    # pd.cut:
# print(decade_cat)
# print(decade_cat.categories)
print(pd.value_counts(decade_cat))

#### make two bins evenly spaced based on the max and min year
#### Cut the years into two bins, state the precision to be within plus or minus one year
cut2 = pd.cut(years, 2, precision=1)
print(pd.value_counts(cut2))