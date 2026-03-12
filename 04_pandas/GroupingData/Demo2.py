import pandas as pd

data = {
    'Player':["Virat","Kohli","Dhoni","Rahul","Rohit"],
    'Rank':[1,4,2,5,3],
    'Year':[2000,2001,2002,2003,2004]
}
df = pd.DataFrame(data)
print("Player's info:\n",df)

res = df.groupby('Player')

print("\n",res.first())

for name,group in res:
    print(name)
    print(group)