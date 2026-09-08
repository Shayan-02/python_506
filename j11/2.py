"""
voroodi nadarad
khorooji nadarad
"""
def say_hello():
    # print("hello", "world")
    print("hello world")


"""
voroodi darad
khorooji nadarad
"""
def say_hello2(name, family):
    print(f"hello {name} {family}")


"""
voroodi darad
khorooji darad
"""
def double(num):
    return num * 2


"""
voroodi nadarad
khorooji darad
"""
def say_hello4():
    return "hello world"

say_hello()
say_hello2("sara", "kabiri")


number = int(input("enter a number: "))
x = double(number)
print(x * 2)

print(say_hello4())