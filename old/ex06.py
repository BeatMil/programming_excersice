def check_int(prompt): # check if input is number or not
	while True:
		num = input(prompt)
		if num.isdigit():
			return int(num)
		else:
			print("ENTER AN INTEGER")

num1 = check_int("num1: ")
num2 = check_int("num2: ")
add = num1 + num2
minus = num1 - num2
times = num1 * num2
divide = num1 / num2
print("%s + %s = %s"%(num1,num2,add))
print("%s - %s = %s"%(num1,num2,minus))
print("%s * %s = %s"%(num1,num2,times))
print("%s / %s = %s"%(num1,num2,int(divide)))