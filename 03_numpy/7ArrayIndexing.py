import numpy as np

print("\nFor 1-D array\n")

x = np.array([1,2,3,4,5])
print(x)
print(x[0])
print("Last element = ",x[-1]) #Returns last element

print("\nFor 2-D array\n")

n = np.array([[11,23,36,48,59],[16,27,78,39,10]])
print(n)
print(n[0,0])
print(n[1,3])
print(n[1,2])
print("Last element of 1st row= ",n[0,-1]) #Returns last element of 1st row
print("Last element of 2nd row= ",n[1,-1]) #Returns last element of 2nd row
print("Dimension = ",n.ndim)

print("\nFor 3-D array\n")

m = np.array([[[14,21,36],[48,53,69]],[[13,22,6],[7,12,90]]])
print(m)
print(m[0,0,1])
print(m[1,0,2])
print(m[0,1,2])
print("Dimension = ",m.ndim)