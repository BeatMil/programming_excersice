from random import randint

print("gacha game17!!!")
print("_"*80)

inventory = []

while(True):
    ran_num = randint(0,10)
    print(ran_num)
    user_input = input("PRESS ENTER")

    # let user exit the game
    # by user I mean me ;w;
    if (user_input == ""):
        pass
    else:
        print("exiting...")
        break


    if inventory.count(ran_num) > 0:
        print("same number")
    else:
        inventory.append(ran_num)

    inventory.sort()
    print(inventory)

    if (len(inventory) >= 11):
        print("CONGRATS!")
        break
