class ParentClass:
    def parent_method(self):
        print("This is a parent method.")
    
class ChildClass(ParentClass):
    def parent_method(self):
        print("Rocky")
        super().parent_method()
    def child_method(self):
        print("This is a child method.")
        super().parent_method()

child_obj=ChildClass()
child_obj.child_method()