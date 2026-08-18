a = input()
b = ""
asghar = len(a) - 1

while asghar >= 0:
    b += a[asghar]
    asghar -= 1

print("YES" if a == b else "NO")