# print prime-number
for i in range(1000):
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i)
    elif i%2 != 0:
        if i%3 != 0:
            if i%5 != 0:
                if i%7 != 0:
                    print(i)
