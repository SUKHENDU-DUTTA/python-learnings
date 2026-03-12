import numpy as np

print("For 0-D array:\n")
x = np.array(10)

print(x)
print(x.ndim)
print(x.shape)

print("\nFor 1-D array:\n")

x1 = np.array([10,20,30])

print(x1)
print(x1.ndim)
print(x1.shape)

print("\nFor 2-D array:\n")

x2 = np.array([[10,20,30],[40,50,60]])

print(x2)
print(x2.ndim)
print(x2.shape)

print("\nFor 3-D array:\n")

x3 = np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])

print(x3)
print(x3.ndim)
print(x3.shape)