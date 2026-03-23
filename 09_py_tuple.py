"""
1.A tuple is a collection which is ordered and unchangeable (Immutable).
    It's one type of data structure in Python that is used to store multiple items in a single v
   In Python tuples are written with round brackets.
2. We declare tuple with () and separate items with commas.
3. Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
4. We can use negative indexing to access the tuple items.
5. We can use the tuple() constructor to make a tuple.
6. Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
7. Tuple items can be of any data type, and a tuple can contain different data types.
8. A tuple can also contain other tuples, which is called a nested tuple.
9. There is no built-in tuple method to add items, but we can use the + operator to concatenate two tuples.
   Basically not Modify/delete/update but Create a new tuple with the added item(s).
10. We can use the len() function to determine how many items a tuple has.
11.tuple has only two built-in methods: count() and index().
12.tuple.count(x) - Returns the number of times a specified value occurs in a tuple.
13.tuple.index(x) - Searches the tuple for a specified value and returns the position of where it was found.
14. We can use the del keyword to delete the tuple completely.
15. We can loop through the tuple items by using a for loop.
16. Below List of tuple methods:
    len() - Returns the number of items in a tuple.
    count() - Returns the number of times a specified value occurs in a tuple.
    index() - Searches the tuple for a specified value and returns the position of where it was found.
    membership operator in - Returns True if a specified value is present in the tuple.
    membership operator not in - Returns True if a specified value is not present in the tuple.
    iter() - Returns an iterator object.
    repetition operator * - Returns a tuple with the specified number of occurrences of an item.
    is object - Returns True if both variables are the same object, otherwise False.
    is not object - Returns True if both variables are not the same object, otherwise False.
    sorted() - Returns a sorted list of the specified iterable's items.
17. tuple -> has zip function.
18. to see entire method of tuple then use dir(tuple)
19. In List have feature called "List Comprehension" but in tuple doest have this feature.
20. To handle tuple comprehension feature using "generator" techniq will solve it.

"""

# Create a tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print(type(my_tuple))

# Accessing tuple items
print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana
print(my_tuple[2])  # Output: cherry

# Iterating through a tuple
for item in my_tuple:
    print(item)

# Tuple with different data types
my_tuple2 = ("Hello", 42, 3.14, True)
print(my_tuple2)

# Nested tuple
nested_tuple = ("apple", "banana", ("cherry", "grape"))
print(nested_tuple)
print(nested_tuple[2])  # Output: ('cherry', 'grape')
print(nested_tuple[2][0])  # Output: cherry

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3

# Convert tuple to list and back to tuple
my_tuple3 = (1, 2, 3)
my_list = list(my_tuple3)  # Convert tuple to list
my_list.append(4)  # Modify the list
my_tuple3 = tuple(my_list)  # Convert back to tuple
print(my_tuple3)  # Output: (1, 2, 3, 4)

# Tuple methods
my_tuple4 = (1, 2, 3, 2, 4)
print(my_tuple4.count(2))  # Output: 2
print(my_tuple4.index(3))  # Output: 2

# Deleting a tuple
my_tuple5 = (1, 2, 3)
del my_tuple5
# print(my_tuple5)  # This will raise an error because the tuple has been deleted

# tuple with length
my_tuple6 = (1, 2, 3, 4, 5)
print(len(my_tuple6))  # Output: 5

# tuple with membership operator
print(3 in my_tuple6)  # Output: True
print(6 in my_tuple6)  # Output: False

# tuple with repetition operator
my_tuple7 = (1, 2, 3)
repeated_tuple = my_tuple7 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

print(sorted(repeated_tuple))  # Output: (1, 1, 2, 2, 3, 3)

# tuple with is and is not operator
my_tuple7 = (1, 2, 3)
my_tuple8 = (1, 2, 3)
print(my_tuple7 is my_tuple8)  # Output: False
print(my_tuple7 is not my_tuple8)  # Output: True


# tuple with iter() function
my_tuple8 = (1, 2, 3)
my_iterator = iter(my_tuple8)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3

# tuple with comparision operators
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3, 4)
print(tuple_a == tuple_b)  # Output: False
print(tuple_a != tuple_b)  # Output : True

# tuple zip function
list1 = [1, 2, 3, 4, 7]
list2 = [5, 6, 7, 8]
t = tuple(zip(list1, list2))
print("final zip values", t)

# tuple dir
print(dir(tuple))

# tuple, using generator
list3 = [5, 6, 7, 8]
z = (x for x in list3 if x % 2 == 0)  # this is not tuple. it's generator.
print(z, list(z))  # z generator object and list(z)  convert generator to list object.
