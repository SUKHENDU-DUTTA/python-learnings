# import numpy as np
import pandas as pd

data = ["Jacob","Amit","ROCKY","SaM","KiRAn"]

series = pd.Series(data)
print("\n New Dataframe: \n",series)

print("Searching\n",series.str.contains("ROCKY"))