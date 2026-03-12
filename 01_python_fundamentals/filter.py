def filter_fun(a):
    return a>4


l=[1,2,3,5,7,11,13]

newl=list(filter(filter_fun,l))
print(newl)