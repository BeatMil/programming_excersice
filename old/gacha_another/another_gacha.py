from random import randint
from os import path
inventory = []
while True:
	option = input("PRESS ENTER; (S)ave, (L)oad")
	if option == "":
		random_num = randint(1,10)
		if inventory.count(random_num) > 0: # if got same number
			print("same number", random_num)
		else: # if got new number
			inventory.append(random_num)
			print(random_num)
		inventory.sort()
		print(inventory)
		if len(inventory) >= 10:
			print("Congratulations!")
			break
	elif option.lower() == "s":
		lever = True # if file exist helper line27
		file_name = input("file name: ")
		file_name += ".gac" # add file extention
		if path.exists(file_name):
			print("file %s already exists"%file_name[0:-4])
			option = input("Override %s? (Y),(N)\n"%file_name).lower()[0]
			print(option)
			if option == 'y': # if yes
				pass
			else: # if no
				lever = False
		if lever:
			with open(file_name,'w') as file:
				for i in inventory:
					file.write("%s,"%i)
			print("save completed")
	elif option.lower() == "l": # load number from csv file to array inventory
		inventory.clear() 
		file_name = input("file: ")
		file_name += ".gac" # add file extention
		if path.exists(file_name):
			with open(file_name,'r') as file:
				save_data = file.read()
				if save_data:
					save_array = save_data.split(',')
					for i in save_array:
						inventory.append(i)
					inventory.pop(-1)
					print(inventory)
				else:
					print("File is empty.")
		else:
			print("file not exists")
