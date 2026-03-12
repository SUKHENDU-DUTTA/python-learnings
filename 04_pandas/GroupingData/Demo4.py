import pandas as pd
import numpy as np
data = {
    'Player':["Virat","Kohli","Dhoni","Rahul","Rohit"],
    'Rank':[1,4,2,5,3],
    'Year':[2000,2001,2002,2003,2004],
    'Points':[10,20,30,40,50]
}
df = pd.DataFrame(data)
print("Player's info:\n",df)

groupRes = df.groupby('Year')
print("Aggregate Data: \n",groupRes['Points'].agg(np.mean))