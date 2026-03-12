import pandas as pd

data = {'Students': ["Amit","Raj","Subham","Jacob","David"],
        'ID':['S01', 'S02', 'S03', 'S04','S05'],
        'Rank':[1,2,3,4,5],
        'Marks':[98,79,86,62,99],
        'Address':["East","West","South","North","South-East"]}

df = pd.DataFrame(data,index=['R1','R2','R3','R4','R5'])
print("Student Record: \n",df)

result = df.sort_values(by='Marks')
print("Updated Student Record: \n",result)