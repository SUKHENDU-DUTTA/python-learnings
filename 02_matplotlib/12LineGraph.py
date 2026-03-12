import matplotlib.pyplot as plt
import numpy as np

months = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
rain = np.array([10,15,15,10,12,18,20,19,23,21,10,14])

plt.plot(months,rain)

plt.title('Rainfall in mm')

plt.xlabel('Month')
plt.ylabel('Rainfall in mm')

plt.show()