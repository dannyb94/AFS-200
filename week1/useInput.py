# Step 3: Manipulate string
# asks the user to input their “name” and “age”
# prints out a message that states their name, age, and in what year they will turn 100 years old (ex. Hi *name*, you are *age* years old, and will turn 100 years old in *year*

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hundred = str((2021 - age) + 100)

print("Hola " + name + ".  You'll be 100 years old in " + hundred + ".")