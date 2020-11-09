from random import randint as rd

inventory = []
print("Welcome to another %s"%__file__)
while(True):
    ran_num = rd(1,10)
    if inventory.count(ran_num) > 0:
        print("DUP: %s"%ran_num)
    else:
        inventory.append(ran_num)
        inventory.sort()
        print(inventory)
    if len(inventory) >= 10:
        break
print("you win!")
