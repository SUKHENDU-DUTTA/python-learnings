import pandas as pd

data1 = {'id':["S01","S02","S03","S04","S05"],
         'student':["Amit","Suraj","Binod","Manoj","Shyam"],
         'Rank':[1,2,3,4,5]}
data2 = {'id':["S06","S07","S08","S09","S10"],
         'student':["Raj","Subham","Rinku","Virat","Sundar"],
         'Rank':[6,7,8,9,10]}

dataframe1=pd.DataFrame(data1,index=["Student1","Student2","Student3","Student4","Student5"])
print("DataFrame1 = \n",dataframe1)

dataframe2=pd.DataFrame(data2,index=["Student6","Student7","Student8","Student9","Student10"])
print("\nDataFrame1 = \n",dataframe2)

resDF = pd.concat([dataframe1,dataframe2])
print("\n Joined DataFrame using concatenate: \n",resDF)