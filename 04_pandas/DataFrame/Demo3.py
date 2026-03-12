
#The dataframe.iloc is used to access  a group of rows and columns by integers. We have also set column and index.
import pandas as pd

data = {'student':["Amit","Suraj","Prakash","David","Steve"],
        'rank':[2,1,5,3,4],
        'score':[89,82,33,54,91]}

df1 = pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records \n\n",df1)

#Access using row and column by integer position

print("\n Values = \n",df1.iloc[[1,2]])