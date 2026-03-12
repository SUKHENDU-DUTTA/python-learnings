import numpy as np
import pandas as pd

s=pd.Series(["P","Q","R","S"],dtype="category")
print("Series: \n",s)

s=s.cat.add_categories(["A","B","C","D"])
print("Updated Series: \n",s)