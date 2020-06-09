# it works!!! yayyy
def factorial(number):
    print(number)
    if number > 0:
        factorial(number - 1)

def factwo(number):
    if number >= 0:
        factwo(number - 1)
        print(number)

factwo(10)