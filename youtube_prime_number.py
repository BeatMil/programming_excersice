
def is_prime():
    for num in range(100):
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)

is_prime()