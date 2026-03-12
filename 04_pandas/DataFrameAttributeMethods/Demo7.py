import pandas as pd

data={'student':["Rinku","Pinku","Tinku","David","John","Rohan","Raj","Subham","Suraj","Sundar"],
      'ranks':[1,2,3,4,5,6,7,8,9,10],
      'score':[95,92,83,74,59,69,78,88,99,67]}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE','RowF','RowG','RowH','RowI','RowJ'])
print("Student Records: \n\n",df)

print("1st 5 Rows: \n\n",df.head())  #This line print the first 5 rows