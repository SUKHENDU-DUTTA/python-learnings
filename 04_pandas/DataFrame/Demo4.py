#The index argument is used to set name your own indexes in a dataframe.

import pandas as pd

data = {'student':["Amit","Suraj","Prakash","David","Steve"],
        'rank':[2,1,5,3,4],
        'score':[89,82,33,54,91]}

df1 = pd.DataFrame(data,index=['Student1','Student2','Student3','Student4','Student5'])
print("Student Records \n\n",df1)
