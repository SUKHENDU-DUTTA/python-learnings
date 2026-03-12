import numpy as np

print("Using CONCATENATE Method:\n")

n1 = np.array([1,2,3,4,5,6,7,8,9])
n2 = np.array([10,11,12,13,14,15,16,17,18])

print(f"1st Array:\n{n1}\n")
print(f"2nd Array:\n{n2}\n")

# print("Iterating 1st Array:\n")
# for i in n1:
#     print(i)
#
# print("Iterating 2nd Array:\n")
# for i in n2:
#     print(i)

newarray = np.concatenate((n1,n2))

print("Joined Array using concatenate:\n")
print(newarray)

print("Using stack Method:\n")

rearray = np.stack((n1,n2))
print("After Joining using stack method:\n",rearray)

print("Using hstack Method:\n")

rearray1 = np.hstack((n1,n2))
print("After Joining using hstack method:\n",rearray1)

print("Using vstack Method:\n")

rearray2 = np.vstack((n1,n2))
print("After Joining using vstack method:\n",rearray2)

print("Using dstack Method:\n")

rearray3 = np.dstack((n1,n2))
print("After Joining using dstack method:\n",rearray3)

print("Using column_stack Method:\n")

rearray4 = np.column_stack((n1,n2))
print("After Joining using hstack method:\n",rearray4)