import pandas as pd

data = [10,20,30,40,50]
s=pd.Series(data,name="Series",index=["Num1","Num2","Num3","Num4","Num5"])

print("Series: \n",s)
print("\n Series Info \n ",s.info())