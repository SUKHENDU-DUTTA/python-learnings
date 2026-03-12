import pandas as pd

data = [10,20,30,40,50,60,70,80,90]
data1 = [15,25,35,45,55,65,70,80,90]

series = pd.Series(data)
series2 = pd.Series(data1)

print("Series 1: \n",series)
print("Series 2: \n",series2)

def demo(x,y):
    if(x>y):
        return x
    else:
        return y

res = series.combine(series2,demo)
print("After combine: \n",res)