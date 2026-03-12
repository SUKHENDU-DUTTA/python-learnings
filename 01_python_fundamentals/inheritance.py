class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of employee {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")


e1=Employee("Sukhendu",420)
e1.showDetails()
e2=Programmer("Rocky",410)
e2.showDetails()
e2.showLanguage()