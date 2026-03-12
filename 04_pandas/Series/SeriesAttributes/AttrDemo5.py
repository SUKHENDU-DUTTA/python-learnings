import numpy as np
import pandas as pd

data = [10,20,30,40,50,np.nan]
s=pd.Series(data)

print("Series: \n",s)
print("\n Series DataType :",s.hasnans)