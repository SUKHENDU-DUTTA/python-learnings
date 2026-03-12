import pandas as pd

df = pd.read_csv("C:/Users/Sukhendu/Desktop/Student.csv", index_col="Student")

print("Our dataframe: \n",df)

res = df.iloc[2]
print("\n",res)