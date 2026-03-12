import pandas as pd

data = {'student':["Amit","Suraj","Prakash","David","Steve"],
        'rank':[2,1,5,3,4],
        'score':[89,82,33,54,91]}

# The DataFrame is a 2-D, tabular data, table with rows and column.
#The dataframe() , method is used to create a DataFrame and has the parameters like data, index, columns, dtype, copy, etc.
df = pd.DataFrame(data)
print("Student Records \n\n",df)
