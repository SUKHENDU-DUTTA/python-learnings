import pandas as pd

data={'student':["Rinku","Pinku","Tinku","David","John"],
      'ranks':[1,2,3,4,5],
      'score':[95,92,83,74,59]}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records: \n\n",df)

print("Shape: \n\n",df.shape)  #This line print the dimensionality of the dataframe in the form of a tuple