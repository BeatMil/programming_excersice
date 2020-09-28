#Write a Java program that takes a number as input and prints its multiplication table upto 12
num = int(input("int: "))
for i in range(1,13):
    print("%s * %s = %s"%(num,i,(num*i)))