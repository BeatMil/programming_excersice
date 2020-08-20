import random
inventory = []
while True:
    input("PRESS ENTER")
    rand_num = random.randint(0,10)
    if inventory.count(rand_num) > 0:
        print("same number")
    else:
        inventory.append(rand_num)
    inventory.sort()
    print(rand_num)
    print(inventory)
    print()
    if len(inventory) >= 10:
        break
print("YOU WIN~")
