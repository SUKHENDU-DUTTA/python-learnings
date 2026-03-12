import numpy as np

print("Removing elements from arrays using setdiff1d() method:\n ")
n1 = np.array([11,23,3,14,50])
n2 = np.array([3,50,30,17,23])

print("First Array:\n",n1)
print("Second Array:\n",n2)

diff = np.setdiff1d(n1,n2)
print("Removing the element of n2 from n1:\n",diff) #It removes the element of n2 from n1

diff2 = np.setdiff1d(n2,n1)
print("Removing the element of n1 from n2:\n",diff2)  #It removes the element of n1 from n2
