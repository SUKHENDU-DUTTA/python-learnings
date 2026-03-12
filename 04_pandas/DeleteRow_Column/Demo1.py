import pandas as pd

data = {'Students': ["Amit","Raj","Subham","Jacob","David"],
        'ID':['S01', 'S02', 'S03', 'S04','S05'],
        'Rank':[1,2,3,4,5],
        'Marks':[98,90,86,75,64],
        'Address':["East","West","South","North","South-East"]}

df = pd.DataFrame(data)
print("Student Record: \n",df)

resDF = df.drop('Marks',axis='columns')
print("Updated Student Record: \n",resDF)