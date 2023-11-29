
l_1 = [1,11,14,5,8,9]
l_2 = []

def lessThanTen():
    for i in l_1:
        if i < 10:
            l_2.append(i)
        elif i >= 10:
            continue
    
print(lessThanTen())
    