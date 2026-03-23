"""
1. List is one type of data structure in Python. It is a collection which is ordered and changeable. Allows duplicate members.
2. Lists are written with square brackets. Ex: [1, 2, 3]
3. List stores items in a particular order. You can access items in a list by referring to the index number, inside square brackets. The first item has index 0, the second item has index 1, and so on.
4. List can store different types of data, such as integers, strings, and even other lists. You can also use negative indexing to access items from the end of the list. For example, -1 refers to the last item, -2 refers to the second last item, and so on.
5. Lists are mutable, which means you can change their content without changing their identity. You can add
6. List can be Forward and Backward Traversal.
   You can use a for loop to iterate through the items in a list.
   You can also use the built-in functions like len() to get the number of items in a list, and the append() method to add an item to the end of a list.
7. List allows duplicate members. This means that you can have multiple occurrences of the same value in a list. For example, [1, 2, 2, 3] is a valid list with duplicate members.
8. List can be nested, which means you can have a list within a list. This allows you to create more complex data structures. For example, [[1, 2], [3, 4]] is a nested list containing two inner lists.
9. List support  Slicing, which allows you to access a range of items in a list. You can specify the start and end index to slice a portion of the list. For example, my_list[1:4] will return a new list containing the items from index 1 to index 3 (excluding index 4).
10. List start with index 0, which means the first item in the list is accessed with index 0. This is a common convention in programming languages and allows for easy access to list items using their position in the list.
11. List start with Index o and last element of list is accessed with index -1. This allows you to easily access the last item in the list without needing to know the length of the list.
     Formula forword index will be : 0,1,2,3...n-1
     Formula backward index will be : -1,-2,-3...-n
12. List can be  allow to modify the list after it has been created. You can add, remove, or change items in a list using various methods and operations. For example, you can use the append() method to add an item to the end of a list, or the remove() method to remove a specific item from the list.
13. List can be used to store a collection of items that are related to each other. For example, you can use a list to store a list of names, a list of numbers, or a list of objects. This allows you to organize and manage your data in a structured way.
14. List can be sliceable, which means you can create a new list by slicing a portion of an existing list. This allows you to extract specific items from a list and create a new list based on those items. For example, my_list[1:4] will return a new list containing the items from index 1 to index 3 (excluding index 4).
     we can call as S3, [Start:Stop:Step]
     Ex: my_list[0:5:2] will return a new list containing every second item from index 0 to index 4 (excluding index 5).
15. List provides various built-in methods that allow you to perform operations on the list. Some common methods include:
     append(): Adds an item to the end of the list.
     insert(): Inserts an item at a specified index in the list.
     remove(): Removes the first occurrence of a specified item from the list.
     pop(): Removes and returns the item at a specified index (or the last item if no index is specified).
     sort(): Sorts the items in the list in ascending order.
     reverse(): Reverses the order of the items in the list.
     count(): Returns the number of occurrences of a specified item in the list.
     index(): Returns the index of the first occurrence of a specified item in the list.
     delete(): Deletes an item at a specified index from the list.
     clear(): Removes all items from the list.
     append(): Adds an item to the end of the list.
     extend(): Adds all items from another list to the end of the current list.
16. List Comprehansion : This one of the techniq in python insted of writing traditional way.
       Syntax: new_list = [expression for item in iterable if condition]
17. dir(list) -- if we want to see what are methods available in list then can check with this syntax.

"""

# Example of a list in Python
my_list = [1, 2, 3, "Hello", [4, 5], True]
# Accessing items in a list
print(my_list[0])  # Output: 1
print(my_list[3])  # Output: 'Hello'
# Modifying a list
my_list[1] = "World"
print(my_list)  # Output: [1, 'World', 3, 'Hello', [4, 5], True]
# Adding an item to the end of the list
my_list.append("New Item")
print(my_list)  # Output: [1, 'World', 3, 'Hello', [4, 5], True, 'New Item']
# Removing an item from the list
my_list.remove(3)
print(my_list)  # Output: [1, 'World', 'Hello', [4, 5], True, 'New Item']
# Slicing a list
sliced_list = my_list[1:4]
print(sliced_list)  # Output: ['World', 'Hello', [4, 5]]
# Iterating through a list
for item in my_list:
    print(item)
# Output:
# 1
# 'World'
# 'Hello'
# [4, 5]
# True
# 'New Item'

# List with duplicate members
duplicate_list = [1, 2, 2, 3, 4, 4, 4]
print(duplicate_list)  # Output: [1, 2, 2, 3, 4, 4, 4]

# remove Duplocate members from list
unique_list = list(set(duplicate_list))
print(unique_list)  # Output: [1, 2, 3, 4]

# Nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
print(nested_list)  # Output: [[1, 2], [3,  4], [5, 6]]
# Prepare a list of from each nested list of First element of each nested list
first_elements = [sublist[0] for sublist in nested_list]
print(first_elements)  # Output: [1, 3, 5]
# Same thing, Last element of each nested list
last_elements = [sublist[-1] for sublist in nested_list]
print(last_elements)  # Output: [2, 4, 6]

# List pop  method
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.pop()  # Removes and returns the last item
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.pop(0)  # Removes and returns the item at index 0
print(my_list)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# List sort method
my_list = [5, 2, 9, 1, 5, 6]
my_list.sort()  # Sorts the list in ascending order
print(my_list)  # Output: [1, 2, 5, 5, 6, 9]
my_list.sort(reverse=True)  # Sorts the list in descending order
print(my_list)  # Output: [9, 6, 5, 5, 2, 1]

# List reverse method
my_list = [1, 2, 3, 4, 5]
my_list.reverse()  # Reverses the order of the list
print(my_list)  # Output: [5, 4, 3, 2, 1]

# List count method
my_list = [1, 2, 2, 3, 4, 4, 4]
count_2 = my_list.count(2)  # Counts the number of occurrences of
print(count_2)  # Output: 2
count_4 = my_list.count(4)  # Counts the number of occurrences of
print(count_4)  # Output: 3

# List index method
my_list = [1, 2, 3, 4, 5]
index_3 = my_list.index(3)  # Returns the index of the first occurrence of 3
print(index_3)  # Output: 2
# List clear method
my_list.clear()  # Removes all items from the list
print(my_list)  # Output: []

# List extend method
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Adds all items from list2 to the end of list1
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# List insert method
my_list = [1, 2, 4, 5]
my_list.insert(2, 3)  # Inserts 3 at index 2
print(my_list)  # Output: [1, 2, 3, 4, 5]


# List delete method
my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Deletes the item at index 2
print(my_list)  # Output: [1, 2, 4, 5]

# List slicing with step
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = my_list[
    0:10:2
]  # Slices the list from index 0 to index 9 with a step of 2
print(sliced_list)  # Output: [0, 2, 4, 6, 8]

# List slicing with negative step
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = my_list[
    9:0:-2
]  # Slices the list from index 9 to index 1 with a step of -2
print(sliced_list)  # Output: [9, 7, 5, 3, 1]

# List slicing with negative step and including the first element
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = my_list[
    9::-2
]  # Slices the list from index 9 to index 0 with a step of -2
print(sliced_list)  # Output: [9, 7, 5, 3, 1]

# list comprehension
# List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an iterable, while optionally filtering items using a condition. The syntax for list comprehension is as follows:
# new_list = [expression for item in iterable if condition]
# Example of list comprehension to create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Example of list comprehension with a condition to create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# check what are operatons in list
print(dir(list))

# List comprehension
# new_list = [expression for item in iterable if condition]
# Tradtional way - suppose we want to print even numbers from list.
list_values = [2, 4, 6, 7, 8, 9, 15]
new_list = []
for i in list_values:
    if i % 2 == 0:
        new_list.append(i)
print("Even Number List: ", new_list)
# Using List Comprehension
z = [y for y in list_values if y % 2 == 0]
print("List comprehension - Event List: ", z)
