def string_to_number(text: str):
    x = text.split(" ")
    for i, y in enumerate(x):
        x[i] = int(y)

    return x

test_case = int(input()) # dodge the mix up
for i in range(test_case):
    ########################
    pass
    ########################

first_line = input()
array_line = input()

command = string_to_number("5 2")
array = string_to_number(array_line)
rotation = command[1]

for i in range(0,rotation):
    box = array[-1]
    array.pop()
    array.insert(0,box)

for i in array:
    print(i,end=" ")
