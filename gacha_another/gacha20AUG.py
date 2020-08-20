import random as r
inventory = []
print("gacha")
print("_"*50)
while True:
    print(inventory)
    input("PRESS ENTER")
    random_num = r.randint(0,9)
    if inventory.count(random_num) > 0:
        print("same %s"%random_num)
    else:
        inventory.append(random_num)
    inventory.sort()
    if len(inventory) >= 10:
        print("you win!")
        break
