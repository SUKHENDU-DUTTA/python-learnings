from numpy import random

print("Random number: ")
n =random.randint(10)
print(n)

print("To get 3 random numbers: ")
n1 = random.randint(10,size=(3))
print(n1)

print("Get random number from array: ")
n2 = random.choice([10,12,17,29,30,45,76,89,90,100])
print(n2)