import pandas as pd

data = {'Students': ["Amit","Raj","Subham","Jacob","David"],
        'Rank':[1,2,3,4,5],
        'Marks':[98,90,86,75,64]}

df = pd.DataFrame(data)
print("Student Record: \n",df)

print("Selecting 2 columns: \n",df[['Rank','Marks']])