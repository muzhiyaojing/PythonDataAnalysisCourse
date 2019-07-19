import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.DataFrame({'city':['Alma','Brian Head','Fox Park'],
                       'altitude':[3158,3000,2762]})

print(dframe)

# Add a new column for each state that the city is in

state_map ={'Alma':'Colorado','Brian Head':'Utah', 'Fox Park':'Wyoming'}

dframe['state'] = dframe['city'].map(state_map)

print(dframe)

# Mapping is a great way to do element wise tranformations and other data cleaning operations