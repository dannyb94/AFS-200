# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

n = int(input("Enter a number: "))

if (n % 2) == 0:
    print("The value {0} is even.".format(n))
else:
    print("The value {0} is odd.".format(n))

# Extras:
# If the number is a multiple of 4, print out a different message.
if (n % 4 == 0):
    print("Input is divisible by 4!")
else:
    print("This output is problematic.")

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter number 1: "))
check = int(input("Enter number 2: "))

if ((num / check) % 2 == 0):
    print("Number 1 divides evenly into Number 2!")
else:
    print("This output is problematic.")
