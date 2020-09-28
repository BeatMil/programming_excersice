# print array in reverse order

# def print_reverse_array(array:list):


long_box = []
length_of_array = int(input(""))
for i in range (length_of_array):
    num = int(input(""))
    long_box.append(num)
long_box.reverse()
for i in long_box:
    print(i)
