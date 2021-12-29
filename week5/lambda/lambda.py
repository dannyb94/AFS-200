# The lambda.py file should have Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def func(f):
    return lambda a: a * f

usr = int(input("Input a number: "))
af = func(usr)
print(af(1))
print(af(2))
print(af(3))
print(af(4))
print(af(5))