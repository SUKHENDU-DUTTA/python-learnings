def appl(fx,value):
    return 6+fx(value)


double=lambda x: x*2
cube=lambda x:x*x*x
print(cube(8))
print(double(3))

print(appl(lambda x:x*x*x,2))