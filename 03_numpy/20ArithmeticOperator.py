import numpy as np

n1 = np.array([10,20,30,40,50])
n2 = np.array([5,10,15,20,25])

print("Array 1:\n",n1)
print("Array 2:\n",n2)

sumarr = np.sum([n1,n2])
print("\nSum of all elements of arrays:\n",sumarr)

addarr = np.add(n1,n2)
print("\nSum of arrays:\n",addarr)

rearr = np.sum([n1,n2],axis=1)
print("\nSum of row elements of arrays:\n",rearr)

subarr = np.subtract(n1,n2)
print("\nSubtraction of arrays:\n",subarr)

mularr = np.multiply(n1,n2)
print("\nMultiplication of arrays:\n",mularr)

divarr = np.divide(n1,n2)
print("\nDivision of arrays:\n",divarr)