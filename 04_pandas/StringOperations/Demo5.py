import numpy as np
import pandas as pd

data = [np.nan,"Jacob","Amit","ROCKY","SaM","KiRAn",np.nan]

series = pd.Series(data)
print("\n New Dataframe: \n",series)

print("Count:\n",series.count())