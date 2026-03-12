import matplotlib.pyplot as plt
import numpy as np

student =np.array(["Vim","John","Amit","Karl","Sam","Suraj"])
marks = np.array([87,90,75,59,99,79])

plt.bar(student, marks)

plt.xlabel('Student')
plt.ylabel('Marks')

plt.title('Student vs Marks')
plt.show()