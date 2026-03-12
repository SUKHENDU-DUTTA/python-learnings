import numpy as np


a = np.array([21,12,32,4,51])
b = np.array([11,24,30,34,15])

print("Array 1:\n",a)
print("\nArray 2:\n",b)

x = a+10
y = b+7

print("\nUpdated Array after adding 10:\n",x)
print("\nUpdated Array after adding 7:\n",y)

p = a - 5
q= b - 10
print("\nUpdated Array after subtracting 5:\n",p)
print("\nUpdated Array after subtracting 10:\n",q)

r = a * 6
print("\nUpdated Array after multiplying 6:\n",r)
s = b * 4
print("\nUpdated Array after multiplying 4:\n",s)

t = a / 4
print("\nUpdated Array after dividing 4:\n",t)
u = b / 5
print("\nUpdated Array after dividing 5:\n",u)