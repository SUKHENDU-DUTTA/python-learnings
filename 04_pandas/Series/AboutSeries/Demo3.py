import pandas as pd

data = [10,20,30,40,50,60,70,80,90]
s= pd.Series(data,index=["RowA","RowB","RowC","RowD","RowE","RowF","RowG","RowH","RowI"])
print("Series of data:\n",s)

