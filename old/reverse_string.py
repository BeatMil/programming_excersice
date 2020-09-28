reversed_text = ''
def reverse_string(text):
    global reversed_text 
    print("len: %s"%len(text))
    if len(text) > 0:
        # print(text[-1], end='') # print without new line
        reversed_text += text[-1] # added last string to the variable
        reverse_string(text[0:-1])
        print('a')
        return reversed_text
    else:
        print('x')
        return 'something'


name = "Anutorn"
# name = name[0:-1]
# print(name[-1])
print(reverse_string(name))