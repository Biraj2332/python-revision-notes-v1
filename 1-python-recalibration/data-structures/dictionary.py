# Dictionary
# Collection of key-value pairs
# Keys must be unique and immutable (strings, numbers, tuples)
# Values can be of any data type and can be duplicated
# Characteristics: Unordered, Mutable, Dynamic
# notation: {key: value, key2: value2, ...}

# Dictionary creation

'''
Creating a Dictionary
Syntax for creating an empty dictionary:

dictionary_name = {}

Copy to clipboard

The dict() function can also be used:

dictionary_name = dict()

Copy to clipboard

Syntax for creating a dictionary with entries:

dictionary_name = { key1: value1,  key2: value2,  key3: value3, ... }

Copy to clipboard

Each item is a key-value pair, separated by a comma.

'''
# empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# dictionary with some key-value pairs
demo_dict = {
    "name": "Ram",
    "age": 30,
    "city": "Kathmandu",
    "hobbies": ["reading", "traveling", "cooking"],
}
print("Demo dictionary:", demo_dict)

# Accessing values using keys
print("Name:", demo_dict["name"])
print("Age:", demo_dict["age"]) 

# check unordered nature
# print(demo_dict[0])
'''
Traceback (most recent call last):
  File "/home/biraj/Desktop/learn-py/1-python-recalibration/data-structures/dictionary.py", line 27, in <module>
    print(demo_dict[0])
          ~~~~~~~~~^^^
KeyError: 0

'''

# Modifying values
demo_dict["age"] = 31
print("Updated age:", demo_dict["age"])

# Check duplication

demo_dict["name"] = "Shyam"
print("Updated name:", demo_dict["name"])

# dict() function
person = dict(name="Sita", age=28, city="Lalitpur")
print("Person dictionary:", person) 

# Food menus 
menuItems ={
    "Pizza": 10.99,
    "Burger": 5.99,
    "Pasta": 8.99,
    "Salad": 6.99
}
# Adding new item
menuItems["Soda"] = 1.99
print("Updated menu:", menuItems)

# changing item price
menuItems["Pizza"] = 11.99
print("New pizza price:", menuItems["Pizza"])

# Removing items 
del menuItems["Salad"]
print("Menu after removing salad:", menuItems)

'''
Iterating a Dictionary
Common methods for iteration:

.keys(): Accesses dictionary keys.
.values(): Accesses dictionary values.
.items(): Accesses key-value pairs.
Syntax
dictionary_name.keys()
dictionary_name.values()
dictionary_name.items()


'''

# Iterating over keys
print("Menu items:")
for item in menuItems.keys():
    print(item)

# Iterating over values
print("\nMenu prices:")
for price in menuItems.values():
    print(price)


# Iterating over key-value pairs
print("\nMenu items and prices:")
for item, price in menuItems.items():
    print(f"{item}: ${price:.2f}")

# Dictionary comprehension
# Syntax: {key_expression: value_expression for item in iterable if condition}
# Dictionary comprehensions provide a concise way to create dictionaries from iterables, allowing
# for filtering and transformation of data in a single line of code.
squared_numbers = {x: x**2 for x in range(1, 6)}
print("Squared numbers:", squared_numbers)

# Food menu with discounted prices using dictionary comprehension
discounted_menu = {item: price * 0.9 for item, price in menuItems.items()}
print("Discounted menu:", discounted_menu)