import pandas as pd

data = ["Jacob","Amit","ROCKY","SaM","KiRAn"]

series = pd.Series(data)
print("\n New Dataframe: \n",series)

print("Converting Strings to Uppercase:\n",series.str.upper())