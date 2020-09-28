import os
from time import sleep


def check_file(file_name):
    list_dir = os.listdir()
    for i in list_dir:
        if i == file_name:
            return True
    return False


print("--"*20)
print("MONIKA MANE")
print("--"*20)

# check if file monika.txt exist in current directory or not
file_name = "monika.txt"
is_exist = check_file(file_name)

if not is_exist:
    print("creating monika.txt")
    monika = open("monika.txt","w")
    monika.write("delete this file and monika gone")
    monika.close()
else:
    print("file exist")

while True:
    if check_file(file_name):
        print("monika is here")
    else:
        print("monika ded")
        break
    sleep(1)

