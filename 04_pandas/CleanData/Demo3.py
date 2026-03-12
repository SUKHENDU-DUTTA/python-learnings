import pandas as pd

df =pd.read_csv("C:/Users/Sukhendu/Desktop/Demo.csv")

print("Our dataframe: \n",df)

resdf = df.dropna()
print("\n New Dataframe: \n",resdf)