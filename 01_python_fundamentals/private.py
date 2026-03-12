class Employee:
    def __init__(self):
        self.__name ="Sukhendu"

a=Employee()
# print(a.__name)   Cannot access due to private object

print(a._Employee__name)  #Can be accesed indirectly