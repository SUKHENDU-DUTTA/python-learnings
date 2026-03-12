import matplotlib.pyplot as plt
import numpy as np

a =np.arange(5)
b= [2,4,6,8,10]
c=[5,6,7,8,9]

fig =plt.figure()
ax = plt.subplot()

ax.plot(a,b,'k--',label='Frequency')
ax.plot(a,c,'k:',label='Period')

legend = ax.legend(loc='upper center')
legend.get_frame().set_facecolor('red')

plt.title('Frequency of signal')
plt.show()