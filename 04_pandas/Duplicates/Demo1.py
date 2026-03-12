import pandas as pd

data = {
    'Student': ["Amit","Subham","Amit","Deepak","Raj"],
    'Rank':[1,2,1,3,4],
    'Marks':[90,88,90,77,66]
}

df = pd.DataFrame(data)
print("Student Records: \n",df)

rs = df.duplicated()
print("\nDuplicate Data: \n",rs)