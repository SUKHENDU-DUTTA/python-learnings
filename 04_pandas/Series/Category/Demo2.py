import numpy as np
import pandas as pd

df = pd.DataFrame({"cat1": list("pqrs"),"cat2":list("abcd"),"cat3":list("wxyz")},dtype="category")
print("DataFrame Frame: \n",df)

print("Data TYPE OF EACH COLUMN:  \n",df.dtypes)
