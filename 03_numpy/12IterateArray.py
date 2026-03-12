import numpy as np

n = np.array([1,2,3,4,5,6])
print("Iterating 1-D Array:\n")

for i in n:
    print(i)

print("Type = ",type(n))
print("Data Type = ",type(n.dtype))
print("Dimensions = ",n.ndim)

n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nIterating 2-D Array:\n")

for i in n1:
    print(i)

print("Type = ",type(n1))
print("Data Type = ",type(n1.dtype))
print("Dimensions = ",n1.ndim)

n3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Iterating 3-D Array:\n")

for i in n3:
    print("Each Matrics:\n")
    print(i)

print("Type = ",type(n3))
print("Data Type = ",type(n3.dtype))
print("Dimensions = ",n3.ndim)