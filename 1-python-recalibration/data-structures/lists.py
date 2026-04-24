# Lists in python
# Lists can have similar or different data types as elements.
# Characteristics of lists:  Ordered, Mutable, Allows duplicate elements, 
# Can contain elements of different data types, Dynamic size

# Notation: []

# List creation 

myDefaultList = []   # Empty list
print(myDefaultList)  

# List with elements
listsWithElements = [1, 2, 3, 'hello', True]
print(listsWithElements)


# Creating lists using list() constructor
listWithConstructor = list((1,3,4,5,'Hello','World',True, 6.5))
print(listWithConstructor)


# List as ordered 
print(listsWithElements[0])  
print(listsWithElements[1])

# Allow duplicate elements
myNewList = [1,2,3,4,5]
print(myNewList)  
myNewList.append(5)  # Adding duplicate element
print(myNewList)  # Now the list contains a duplicate element

listsWithElements.append('hello') 
print(listsWithElements) 

# Check mutable
# mutable means we can change the contents of the list after it has been created.

fruits = ['apple', 'banana', 'cherry']
print(fruits)  
fruits[0] = 'grape' 
print(fruits)

fruits[1] = 'blackberry'
print(fruits)

fruits[2] = 'strawberry'
print(fruits)


# Adding methods to list
list1 = [1, 2, 3]
list1.append(4) 
print(list1) 


list1.insert(0, 0)   # Insert 0 at index 0 (it inserts with index and value)
print(list1)

list1.insert(5,3.124)
print(list1)

# extend(): used to add multiple elements to the end of a list.

list1.extend([5, 6, 7])
print(list1)

# Removing or deleting elements from a list
#remove()
list1.remove(1)
print(list1)

# pop(): emoves/returns item at a specific index; removes last item if none specified.
popped_item = list1.pop(0)
print(popped_item)

# clear(): removes all items from the list.
demo = ['a', 'b', 'c']
print("Before clear:", demo)

demo.clear()
print("After clear:", demo)

# del keyword: can be used to delete an entire list or specific elements by index.
myList = [10, 20, 30, 40, 50]
print("Before deletion:", myList)
del myList[1] 
print("After deleting index 1:", myList)

# Sort and reverse
# sort() ---> in ascending order, reverse() ---> in decreasing order
unsorted_list = [3, 1, 4, 2, 5,7,16,9,8,10]
unsorted_list.sort()
print("Sorted list:", unsorted_list)

unsorted_list.reverse()
print("Reversed list:", unsorted_list)

# Counting : count()
all_list = [1, 2, 3, 4, 5, 2, 2, 6,4,3,3,3]
count_1 = all_list.count(3)
print("Count of 3:", count_1)

# searching: index(x[, start[, end]]) → Returns index of first occurrence
index_of_2 = all_list.index(2)
print("Index of first occurrence of 2:", index_of_2)

# Copying a list
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)

# Concatenation: using + operator
list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated_list = list_a + list_b
print("Concatenated list:", concatenated_list)

