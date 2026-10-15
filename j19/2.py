class Person:
    def __init__(self, name, age):
        self.esm = name
        self.sen = age
    def info(self):
        return f"my name is {self.esm} and my age is {self.sen}"
    
    def sleep(self):
        return f"{self.esm} is sleeping..."


p1 = Person("ali", 20)
print(p1.esm)
print(p1.sen)
print(p1.info())

p1.esm = "reza"

print(p1.sleep())