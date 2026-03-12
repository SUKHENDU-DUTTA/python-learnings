class Student:
    def __init__(self):
        self._name="Rocky"

    def _funName(self):
        return "Sukhendu"
    
class Subject(Student):
    pass

obj1=Student()
obj2=Subject()

print(obj1._name)
print(obj1._funName())

print(obj2._name)
print(obj2._funName())