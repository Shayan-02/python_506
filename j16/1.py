with open("test.txt",  "r", encoding="utf-8") as f:
    # print(f.readline(1))
    # print(f.readlines(1))
    print(f.read())
    

# with open("./test.txt", "a", encoding="utf-8") as f:
#     f.write("\nسعید")

with open("test2.txt", "x") as f:
    f.write("salam")