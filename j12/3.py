def test(x):
    global a
    global y
    a = 10
    a = x
    y = 30
    return a


print(test(20))
print(a, y)