a = float(input("Enter grade 1 :"))
b = float(input("Enter grade 2 :"))
c = float(input("Enter grade 3 :"))
d = float(input("Enter grade 4 :"))

if 0 <= a <= 20:
    if 0 <= b <= 20:
        if 0 <= c <= 20:
            if 0 <= d <= 20:
                avg = (a + b + c + d) / 4
                if avg > 18:
                    print(f"your average is {avg} -> A")
                elif avg > 16:
                    print(f"your average is {avg} -> B")
                elif avg > 14:
                    print(f"your average is {avg} -> C")
                elif avg > 10:
                    print(f"your average is {avg} -> D")
                else:
                    print("YOU FAILED")
            else:
                print("grade4 is invalid")
        else:
            print("grade3 is invalid")
    else:
        print("grade2 is invalid")
else:
    print("grade1 is invalid")