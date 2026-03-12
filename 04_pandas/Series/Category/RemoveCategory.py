import pandas as pd

s=pd.Series(["P","Q","R","S"],dtype="category")
print("Series: \n",s)

s=s.cat.remove_categories("S")
print("Updated Series: \n",s)