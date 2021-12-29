# The functions.py file should have program with Python functions that accepts a string and calculate the number of upper case letters and lower case letters.
string = input("Enter a string: ")

def uprLwr(string):
    upper = 0
    lwr = 0

    for ltrs in string:
        if ltrs.isupper():
            upper += 1
        elif ltrs.islower():
            lwr += 1
        else:
            pass
    print("String: ", string)
    print("Uppercase: ", upper)
    print("Lowercase: ", lwr)

# print(uprLwr("John Jacob Jingleheimer Smith"))
# print(uprLwr("Betty Botter bought soMe butter. But she saiD the butter’s bitteR"))
print(uprLwr(string))