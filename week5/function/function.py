# The function.py file should have Python function to find the Max of three numbers.
x = int(float(input("Enter first number: ")))
y = int(float(input("Enter second number: ")))
z = int(float(input("Enter third number: ")))

def findMax(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    else:
        return z

nums = str(float(findMax(x, y, z)))

# print(findMax(3, 2.9, 0.4))
print("The max number is: " + nums)