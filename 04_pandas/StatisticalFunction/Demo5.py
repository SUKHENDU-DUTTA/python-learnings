import pandas as pd

marks = {
    'Maths': [98,90,34,50,76,62],
    'English': [88,71,54,38,70,60],
    'Science': [91,88,73,64,50,81]
}

df = pd.DataFrame(marks)
print("Marks of Students:\n",df)

print("Mean marks:\n",df.mean())
