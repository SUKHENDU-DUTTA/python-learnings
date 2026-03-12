import numpy as np

n1 = np.array([1,2,3])
print(n1.dtype)

n2 = np.array(["Sis","Qp","Poaoa","W"]) #U5 means maximum characters in the array
print(n2.dtype)

n3 = np.array(['AS','PPP','ee','rocky'],dtype='S5') #S5 means maximum characters is set as 5 in the array
print(n3.dtype)

n4 = np.array([10,20,30,40])
print(n4)
print(n4.dtype)
x=n4.astype('i')
print(x)
print(x.dtype)