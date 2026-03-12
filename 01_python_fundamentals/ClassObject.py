class Person:
    name="Sukhendu"
    occ="Student"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occ}.")

a=Person()

a.name="Rocky"

# print(a.name,a.occ)

a.info()