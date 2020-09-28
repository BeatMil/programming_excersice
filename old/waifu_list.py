"""
illiya, miyu, kuro -- fate illiya
maika! -- blend s
Tohka -- Date a live
Hana-chan! -- Watashi ni tenshi ga maorita
Chocala, Valina -- Nekopara
Yami -- to love ru
Kurona, Chiru -- gal gun2
Nana, Shizuku, Rin -- Akiba's trip
"""
def read_file():
	with open('waifu_list.py','r') as file:
		return file.read()

data = read_file()
data_splited = data.split('\n')
waifu_list = []
bracket_index = 0 # count the """ so that we can choose waifu list
for i in range(len(data_splited)):
	if data_splited[i] == '"""':
		bracket_index += 1
	else:
		waifu_list.append(data_splited[i])

	if bracket_index >= 2:
		break

for i in waifu_list:
	print(i)