# The class.py file should ask a user their “input”
# In the class.py file, write a code that Print out an input from user in to Upper Case.

class shopping:
    def __init__(groceries, item):
        groceries.item = item

    def getItem(groceries):
        return groceries.item

# Test
# items1 = shopping("avocado, mango, banana")
item = input("Enter a grocery item: ")

print(item.upper())