def sum_text(the_text):
	num_list = the_text.split(" ")
	total = 0
	for i in num_list:
		total += int(i)
	print(total)

line1 = raw_input()
line2 = raw_input()
line3 = raw_input()
sum_text(line1)
sum_text(line2)
sum_text(line3)
# I did it!
