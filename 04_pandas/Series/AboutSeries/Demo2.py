import pandas as pd

data = [10,20,30,40,50,60,70,80,90]
s= pd.Series(data)
print("Series of data:\n",s)

print("Print the value of 2nd index: ",s[2]) #To access a particular value