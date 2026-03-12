with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(0)
    data=f.read(5)
    print(data)