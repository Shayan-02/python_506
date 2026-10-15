class Person:
    def __init__(self, name, age, pid=""):
        self.name = name
        self.age = age
        self.pid = pid
        
    def info(self):
        return f"""
my name is {self.name}.
my age is {self.age} years old.
my personalID is {self.pid}.
    """


p1 = Person(age=20, name="ali rezaee")

print(p1.info().strip())

print("-"*40)

p1.pid = "0987654321"

print(p1.info().strip())
