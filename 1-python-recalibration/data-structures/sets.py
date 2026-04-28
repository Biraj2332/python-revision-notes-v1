# Set
# Characteristics:
# - Unordered collection of unique elements
# - Mutable (can add/remove elements)
# - No duplicate elements allowed
# - Can contain elements of different data types

# Notation: Sets are defined using curly braces {} or the set() constructor.

# Set creation 

# empty set
empty_set = set()
print("Empty set:", empty_set)

demoSet = {     #sets are unique in nature
    1,  
    "Hello",  
    3.14,  
    (1, 2), 
}
print(type(demoSet))  
print("Demo set:", demoSet)
# Check unordered nature
# print(demoSet[0])
'''

Traceback (most recent call last):
  File "/home/biraj/Desktop/learn-py/1-python-recalibration/data-structures/sets.py", line 25, in <module>
    print(demoSet[0])
          ~~~~~~~^^^
TypeError: 'set' object is not subscriptable
'''
# Using frozen set (immutable set)
myFrozenSet = frozenset([1, 2, 3, 4])
print("Frozen set:", myFrozenSet)

# Frozen sets means that we cannot modify the set after its creation. 
# This means we cannot add or remove elements from a frozen set. 
# However, we can perform operations like union, intersection, and difference with frozen sets,
#  just like with regular sets.

# Check : No allow duplication
mySet = {1, 2, 3, 4, 4, 5,5}
print("My set to check duplication: ", mySet)    # removes 2duplicate elements:4,5

# Check mutable nature
mySet.add(6)
print("My set after adding an element: ", mySet)

mySet.remove(2)
print("My set after removing an element: ", mySet)

# All Set methods
# add(), clear(), copy(), difference(), discard(), intersection(), isdisjoint(), issubset(), issuperset(), pop(), remove(), union(), update() etc.

mainSet = {1, 2, 3, 4, 5}
print("Main set: ", mainSet)

# add() method
mainSet.add(6)
print("After adding 6: ", mainSet)

# remove() method
mainSet.remove(3)
print("After removing 3: ", mainSet)

# union() method
anotherSet = {4, 5, 6, 7}
unionSet = mainSet.union(anotherSet)
print("Union of mainSet and anotherSet: ", unionSet)

# intersection() method
intersectionSet = mainSet.intersection(anotherSet)
print("Intersection of mainSet and anotherSet: ", intersectionSet)

# difference() method
differenceSet = mainSet.difference(anotherSet)
print("Difference of mainSet and anotherSet: ", differenceSet)

# check subset and superset
subsetSet = {1, 2}
print("Is subsetSet a subset of mainSet? ", subsetSet.issubset(mainSet))
print("Is mainSet a superset of subsetSet? ", mainSet.issuperset(subsetSet))

# check pop() method
poppedElement = mainSet.pop()
print("Popped element: ", poppedElement)
print("Main set after popping an element: ", mainSet)

# update() method
mainSet.update({7, 8})
print("Main set after update: ", mainSet)

# clear() method
mainSet.clear()
print("Main set after clearing: ", mainSet)