import pandas as pd

data = {'student':["Amit","Suraj","Prakash","David","Steve"],
        'rank':[2,1,5,3,4],
        'score':[89,82,33,54,91]}

# The dataframe.loc is used in pandas to access a group of rows or columns in a DataFrame.
df1 = pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records \n\n",df1)
print("Value = ",df1.loc['RowA','student'])
print("Value = ",df1.loc['RowA','rank'])
print("Value = ",df1.loc['RowA','score'])