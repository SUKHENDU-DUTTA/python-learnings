import pandas as pd

data1 = {'id':["S01","S02","S03","S04","S05"],
         'student':["Amit","Suraj","Binod","Manoj","Shyam"],
         'Rank':[1,2,3,4,5]}
data2 = {'Roll':[101,102,103,104,105],
         'maks':[79,88,90,56,72]}

dataframe1=pd.DataFrame(data1)
print("DataFrame1 = \n",dataframe1)

dataframe2=pd.DataFrame(data2)
print("\nDataFrame1 = \n",dataframe2)

resDF = dataframe1.join(dataframe2)
print("\n Joined DataFrame : \n",resDF)