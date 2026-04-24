
# Tuples: 
# Changeable, ordered, allows duplicates, indexed, immutable
# Notation: ()

# creation of tuples

myDefaultTuple = ()  # Empty tuple
print(myDefaultTuple)

# Tuple with elements
tupleWithElements = (1, 2, 3, 'hello', True)
print(tupleWithElements)

# Creating tuples using tuple() constructor
tupleWithConstructor = tuple((1,3,4,5,'Hello','World',True, 6.5))
print(tupleWithConstructor)

# Tuple as ordered
print(tupleWithElements[0])
print(tupleWithElements[1])

# Check allow duplicate elements
myNewTuple = (1,2,3,4,5)
print(myNewTuple)
myNewTuple = myNewTuple + (5,)  # Adding duplicate element 
print(myNewTuple)  

# Check immutable
fruits = ('apple', 'banana', 'cherry')
print(fruits)
# fruits[0] = 'grape'    
# print(fruits)  

# shows error | because immutable property
'''
Traceback (most recent call last):
  File "/home/biraj/Desktop/learn-py/1-python-recalibration/data-structures/tuples.py", line 32, in <module>
    fruits[0] = 'grape'  
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''



# adding tuples with concatenation operator (+)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2  # Concatenating two tuples
print(result)

# Tuple built-in methods   
#List of all built-in methods for tuples: count(), index()
# tuple.count(x) — count occurrences of value
# tuple.index(x[, start[, end]]) — find first index of value

myTuple = (1,3,5,2,4,6,4,6,7,5,3,7,8,3,2,0,1,9,4,6)
print(myTuple.count(3))   #count()

# index()
print(myTuple.index(4))  

# Slicing and splitting tuples
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(myTuple[0:5])  # Slicing the first 5 elements
print(myTuple[5:])  # Slicing from index 5 to the end
print(myTuple[:5])  # Slicing from the beginning to index 5
print(myTuple[::2])  # Slicing with a step of 2 (every second element)


# split 
mygmail = "ramdahal@gmail.com"
username, domain = mygmail.split('@')
# print(mygmail.split('@'))
print("Username:", username)
print("Domain:", domain)

# tuple repetition
# The repetition operator (*) allows you to create a new tuple by repeating the elements of 
# an existing tuple a specified number of times.

tup1 = (1, 2, 3)
print(tup1)
result = tup1 * 3 
print(result) 


# Packing and unpacking tuples
# Packing: Creating a tuple by assigning multiple values to a single variable.
# Unpacking: Assigning the elements of a tuple to multiple variables in a single statement.

# Packing
tup2= 1,2,3
print(tup2)

# Unpacking
a, b, c = tup2
print("a:", a)
print("b:", b)
print("c:", c)

# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)
print(nested_tuple[2])  