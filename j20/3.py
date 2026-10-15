class Person:
    def __init__(self, name, age, pid=""):
        self.name = name
        self.age = age
        self.pid = pid
    def info(self):
        return f"""my name is {self.name}\nmy age is {self.age}"""
    def eat(self, food):
        return f"{self.name} is eating {food}"


class Student(Person):
    def __init__(self, name, age,major,  pid=""):
        super().__init__(name, age, pid)
        self.major = major
    def info(self):
        return f"{super().info()}\nmy major is {self.major}"
    def eat(self, food):
        return super().eat(food) + " in University"


p1 = Person("reza", 15)

print(p1.eat("kebab"))

s1 = Student("ali", 20, "computer")

# print(s1.name)

print(s1.info())
print(s1.eat("ghomesabzi"))
