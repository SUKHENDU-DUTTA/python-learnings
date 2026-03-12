from functools import reduce

num=[23,34,55,12,22,20]

def mysum(x,y):
    return x+y

sum=reduce(mysum,num)

print(sum)