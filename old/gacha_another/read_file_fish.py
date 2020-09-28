file_name = 'b1.gac'
with open(file_name,'r') as file:
	save_data = file.read()
	if save_data:
		save_array = save_data.split(',')
		for i in save_array:
			print(i)
	else:
		print("File is empty.")
