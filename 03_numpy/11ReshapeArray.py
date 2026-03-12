import numpy as np

print("Converting 1-D array to 2-D array\n")
x = np.array([1,2,3,4,5,6])
print("1-D array: ",x)

reShape = x.reshape(2,3)
print("After reshaping to 2-D array: \n",reShape)

print("Converting 3-D array to 2-D array\n")
x2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3-D array:\n ",x2)

reShape1 = x2.reshape(-1)
print("After reshaping to 1-D array: \n",reShape1)