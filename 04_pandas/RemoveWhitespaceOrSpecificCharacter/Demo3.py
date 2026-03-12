import pandas as pd

data = ["!Raj","Amit\n","Sanju","\tJacob","Kiran"]

series = pd.Series(data)

print("Series\n",series)

print("Strip whitespace:\n",series.str.rstrip("!\n\t"))