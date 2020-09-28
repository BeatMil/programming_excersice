from random import randint
from os import path
inventory = []
while True:
    switch = False # check for the same number helper
    input(inventory)
    random_num = randint(0,10)
    for i in inventory: # loop through array; check for duplicates
        if i == random_num:
            switch = True
            break
    if switch == False: # if there is no duplicates; append the number
        inventory.append(random_num)
    inventory.sort()
    print(random_num)
    if len(inventory) >= 10:
        break
print("Game Over")