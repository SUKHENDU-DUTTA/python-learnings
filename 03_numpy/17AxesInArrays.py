import numpy as np

n = np.array([[19,8,10,2,5],[12,6,20,3,9],[23,12,16,7,6]])
print("Original array:\n",n)

print("Minimum Value:\n",n.min())
print("Minimum value with axis 0 (vertical axis):\n",n.min(axis=0))
print("Minimum value with axis 1 (horizontal axis):\n",n.min(axis=1))