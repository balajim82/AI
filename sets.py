"""
1. set is one type of collection which is unordered, unchangeable, and unindexed.
2. set is written with curly brackets. { } similary to dictionary. Ex: {1, 2, 3}
3. Set is does not allow duplicate values. If you try to add a duplicate value, it will be ignored.
4. Set can contain different data types, but it is not recommended to mix data types in a set.
5. Set is mutable, which means you can add or remove items from a set after it has been created.
6. Set does not support indexing, slicing, or other sequence-like behavior. You cannot access items in a set by their position.
7. Set is a collection of unique items, which means that it cannot contain duplicate values. If you try to add a duplicate value to a set, it will be ignored and the set will remain unchanged.
8. Set is a built-in data type in Python, and it is commonly used for operations such as membership testing, removing duplicates from a list.
9. Set supports mathematical set operations like
    1. union,
    2. intersection
    3. difference
    4. isSubset
    5. isSuperset
    6. symmetricDifference
    7. isDisjoint
10. Set is implemented as a hash table, which means that it provides fast membership testing and insertion of items.
    1. copy
    2. clear
    3. add
    4. remove
    5. discard
    6. pop
    7. update
    8. delete
    9. intersection_update
    10. difference_update
    11. symmetric_difference_update

"""

# Create a set
my_set = {1, 2, 3, 4, 5}
print(my_set)
# Output: {1, 2, 3, 4, 5}

# Add an item to the set
my_set.add(6)
print(my_set)

# Remove an item from the set
my_set.remove(3)
print(my_set)
# Check if an item is in the set
print(4 in my_set)  # Output: True
# Get the length of the set
print(len(my_set))  # Output: 5
# Create another set
another_set = {4, 5, 6, 7, 8}
# Union of two sets
union_set = my_set.union(another_set)
print(union_set)  # Output: {1, 2, 4, 5, 6, 7, 8}
# Intersection of two sets
intersection_set = my_set.intersection(another_set)
print(intersection_set)  # Output: {4, 5, 6}
# Difference of two sets
difference_set = my_set.difference(another_set)
print(difference_set)  # Output: {1, 2}
# Symmetric difference of two sets
symmetric_difference_set = my_set.symmetric_difference(another_set)
print(symmetric_difference_set)  # Output: {1, 2, 7, 8}
# Check if one set is a subset of another set
print(my_set.issubset(union_set))  # Output: True
# Check if one set is a superset of another set
print(union_set.issuperset(my_set))  # Output: True
# Check if two sets are disjoint
print(my_set.isdisjoint(another_set))  # Output: False
# Clear the set
my_set.clear()
print(my_set)  # Output: set()

# set remove vs discard
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # This will remove the element 3 from the set
print(my_set)  # Output: {1, 2, 4, 5}
my_set.discard(4)  # This will remove the element 4 from the set
print(my_set)  # Output: {1, 2, 5}
# my_set.remove(10)  # This will raise a KeyError because 10 is not in the set
my_set.discard(10)  # This will not raise an error, it will simply do nothing
print(my_set)  # Output: {1, 2, 5}

# set  update
my_set = {1, 2, 3, 4, 5}
my_set.add(10)
print(my_set)

my_set.update({20, 30})
print(my_set)
