from random import randint as rd
inventory = []
print("welcome to random number game!;")
while (len(inventory) < 10):
    current_number = rd(1,10)
    if (inventory.count(current_number) > 0):
        print("SAME NUMBER: %s"%current_number)
    else:
        inventory.append(current_number)
    inventory.sort()
    print(inventory)

print("Game Over")
