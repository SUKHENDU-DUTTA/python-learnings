import pandas as pd

data={'student':["Rinku","Pinku","Tinku","David","John","Rohan","Raj","Subham","Suraj","Sundar"],
      'ranks':[1,2,3,4,5,6,7,8,9,10],
      'score':[95,92,83,74,59,69,78,88,99,67]}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE','RowF','RowG','RowH','RowI','RowJ'])
print("Student Records: \n\n",df)

print("Last 5 Rows: \n\n",df.tail())  #This line print the last 5 rows