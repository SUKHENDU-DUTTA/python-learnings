import numpy as np

print("Sorting 1-D array:\n")
arr = np.array([18,2,31,14,25,60,7,80,49,100,11,8,63,41,95])
print("Original array:\n",arr)

ascending = np.sort(arr)
print("Sorted array:\n",ascending)

print("\nSorting string array:\n")
n = np.array(['java','python','C','ReactJS','R','SQL'])
print("Original array:\n",n)

print("Sorted array:\n",np.sort(n))

print("\nSorting 2-D array:\n")
n1 = np.array([[19,8,10,2,5],[12,6,20,3,9]])
print("Original array:\n",n1)
print("Sorted array:\n",np.sort(n1))