import pandas as pd

marks = {
    'Maths': [98,None,34,50,76,62],
    'English': [88,71,54,38,70,None],
    'Science': [91,None,73,64,None,81]
}

df = pd.DataFrame(marks)
print("Marks of Students:\n",df)

print("Count of empty values:\n",df.count())
