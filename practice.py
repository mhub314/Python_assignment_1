

# get prime numbers
# 2 dividers, 1 and itself

prime =[]

for i in range(1,100):
    if i == 2 or i == 3 or i == 5 or i ==7:
        prime.append(i)
    elif i % 3 == 0:
        continue
    elif i % 7 == 0:
        continue
    elif i % 5 == 0:
        continue
    elif i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                if i not in prime:
                    prime.append(i)
print(prime)

