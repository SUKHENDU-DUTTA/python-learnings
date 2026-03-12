class Person:

    def __init__(self,n,o):
        print("Hello World!")
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")
        

a=Person("Sukhendu","Student")
b=Person("Rocky","SE")
a.info()
b.info()