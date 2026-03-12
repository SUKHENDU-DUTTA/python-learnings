#To iterate a Dataframe and display the column names, use for loop.
import pandas as pd

data = {'student':["Amit","Suraj","Prakash","David","Steve"],
        'rank':[2,1,5,3,4],
        'score':[89,82,33,54,91]}

df1 = pd.DataFrame(data,index=['Student1','Student2','Student3','Student4','Student5'])
print("Student Records \n\n",df1)

print("\n Displaying records in columns \n")

for col in df1:
    print(col)