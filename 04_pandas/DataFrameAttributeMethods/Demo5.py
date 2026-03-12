import pandas as pd

data={'student':["Rinku","Pinku","Tinku","David","John"],
      'ranks':[1,2,3,4,5],
      'score':[95,92,83,74,59]}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records: \n\n",df)

print("Index: \n\n",df.index)  #This line print the index of the attribute