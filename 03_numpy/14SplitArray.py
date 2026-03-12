import numpy as np

n1 = np.array([1,2,3,4,5,6,7,8,9,10])

print(n1,"\n")

print("Splitting the array into two parts:\n")
spltarr = np.split(n1,2)

# for i in spltarr:
#     print(i)

print("\nAccess the splitted array individually:\n")

print("Array1: ",spltarr[0])
print("Array2: ",spltarr[1])

n = np.array([[1,2,3,4,5],[6,7,8,9,10]])

rearr = np.array_split(n,2)
print(rearr)

print("\nAccess the splitted array individually:\n")
print("Array1: ",rearr[0])
print("Array2: ",rearr[1])