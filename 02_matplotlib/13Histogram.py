import matplotlib.pyplot as plt
import numpy as np

arr = np.array([10,15,22,24,29,34,36,40,44,47,50,56,60,68,72,75,80,88,90])

plt.hist(arr,bins=[0,20,40,60,80])

plt.xlabel('Marks')
plt.ylabel('Students')
plt.title('Histogram of Marks')
plt.show()