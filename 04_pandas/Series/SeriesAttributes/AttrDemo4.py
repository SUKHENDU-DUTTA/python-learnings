import pandas as pd

data = [10,20,30,40,50]
s=pd.Series(data,name="Series")

print("Series: \n",s)
print("\n Series DataType : ",s.name)