import numpy as np

print("\nFor 1-D array\n")

x = np.array([1,2,3,4,5,6,7,8,9,10])

print(x)
print(x[1:3]) #It sliced the array from index 1 to 2 excluding the index 3
print(x[4:9]) #It sliced the array from index 4 to 8 excluding the index 9

# Stepping and slicing
print("Using step method in slicing in 1-D array\n")
print(x[1:-1:2])

print("\nFor 2-D array\n")

n = np.array([[11,23,36,48,59],[16,27,78,39,10]])
print(n)
print(n[0,1:4])
print("\n\n",n[0:2,1:4])