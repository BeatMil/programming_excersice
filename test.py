# This gacha game gets a lot shorter than the first time lol
# I'm getting better at this!
# Me so gud >///<
import random as rd
inventory = []
while (len(inventory) < 10):
    rand_num = rd.randint(1,10)
    if rand_num not in inventory:
        inventory.append(rand_num)
inventory.sort()
print(inventory)
