import numpy as np

n = np.array([15,24,3,42,55])
n1 = np.array([25,14,13,49,75])

print("\nOriginal array 1:\n",n)
print("\nOriginal array 2:\n",n1)

arrmean1 = np.mean(n)
arrmean2 = np.mean(n1)

print("\nMean of array 1:\n",arrmean1)
print("\nMean of array 2:\n",arrmean2)

print("\nMedian of array 1:\n",np.median(n))
print("\nMedian of array 2:\n",np.median(n1))

print("\nStandard deviation of array 1:\n",np.std(n))
print("\nStandard deviation of array 2:\n",np.std(n1))