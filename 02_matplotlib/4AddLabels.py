import matplotlib.pyplot as plt
import pandas as pd

data ={
    'CricketBat':["SG","BDM","SS","GM","kookaburra","Spartan"],
    'MRP':[2000,2200,2400,2700,2800,3000],
    'WeightInGM':[1100,1200,1250,1350,1400,1500]
}

dataframe = pd.DataFrame(data)

plt.plot(dataframe['MRP'],dataframe['WeightInGM'])

plt.xlabel('Bat price')
plt.ylabel('Bat weight in Gram')

plt.show()