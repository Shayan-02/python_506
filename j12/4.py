def seprator(ls):
    odd_lst = []
    even_lst = []
    
    for i in ls:
        if int(i) % 2 == 0:
            even_lst.append(int(i))
        else:
            odd_lst.append(int(i))
    return even_lst, odd_lst


print(seprator([-2, -1, 0, 1, 2, 3]))