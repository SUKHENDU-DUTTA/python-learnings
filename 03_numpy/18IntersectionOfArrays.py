import numpy as np

print("Intersection of array:\n")
n = np.array([19,8,10,2,5])
n1 = np.array([12,5,20,3,19])
print("1st Array: ",n)
print("2nd Array: ",n1)

rearr = np.intersect1d(n,n1)
print("Intersection of arrays:\n",rearr)

                                                                                