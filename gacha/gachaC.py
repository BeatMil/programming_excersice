from random import randint as rd

# I wanna see the diff
inventory = []
print("welcome to gacha game!")
# folding with zf is so cool
# the true while loop
while (True):
    ran_num = rd(1,10)
    if (inventory.count(ran_num) > 0):
        print("DUP: %s"%ran_num)
    else:
        inventory.append(ran_num)
        inventory.sort()
        print(inventory)

    if len(inventory) >= 10:
        break

print("You win!")
