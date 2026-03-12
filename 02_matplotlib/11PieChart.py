import matplotlib.pyplot as plt
import numpy as np

cricketer = np.array(["Virat","Rohit","Dhoni","Rahul","Yuvraj","Sikhar"])
runs = np.array([84,120,50,49,100,101])

plt.pie(runs, labels=cricketer, autopct='%1.2f%%')

plt.title('Players Runs')
plt.show()