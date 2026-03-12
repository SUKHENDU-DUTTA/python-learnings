import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Temperature': [10,20,22,19,23,24,28,26,17,25],
    'Humidity':    [10,13,16,17,20,22,24,30,34,35],
    'Wind':        [12,23,22,10,9,7,11,16,18,7],
    'Precipitation':[17,20,22,30,35,38,40,55,49,50]
}

df = pd.DataFrame(data)

df.plot()
plt.show()