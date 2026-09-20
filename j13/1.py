"""
1- voroodi nadarad / khorooji nadarad
def test():
    pront("salam")

2- voroodi darad / khorooji nadarad
def test(name):
    print("salam", name)

3- voroodi nadarad / khorooji darad
def test():
    return "salam"

4- voroodi darad / khorooji darad
def test(name):
    return "salam", name
"""
def test(name):
    return f"salam  {name}"

print(test("ali"))