"""
1. A dictionary is a collection of key-value pairs.
  Each key is unique and maps to a value. In Python, dictionaries are created using curly braces {} and key-value pairs are separated by colons (:).
  For example: {'key1': 'value1', 'key2': 'value2'}.
  Ex: {a:123, b:456} is not a valid dictionary because the keys are not enclosed in quotes.
2. You can access values in a dictionary using their corresponding keys.
3. Dictionaries are mutable, meaning you can change their contents after they have been created.
4. Dictionaries are unordered collections, meaning that the order of key-value pairs is not guaranteed.
5. Dictionaries can contain any type of data as values, including other dictionaries, lists, and even functions.
6. keys in a dictionary must be immutable types, such as strings, numbers, or tuples. Values can be of any type.
7. key always be unique in a dictionary. If you try to assign a value to an existing key, it will overwrite the previous value.
8. You can use various methods to manipulate dictionaries, such as adding, removing, and updating key-value pairs.
 Majorly used methods are:
    - dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.
    - dict.values(): Returns a view object that displays a list of all the values in the dictionary.
    - dict.items(): Returns a view object that displays a list of key-value pairs in the dictionary as tuples.
    - dict.get(key, default=None): Returns the value associated with the specified key. If the key is not found, it returns the default value (which is None if not specified).
    - dict.update(other_dict): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
    - dict.pop(key, default=None): Removes and returns the value associated with the specified key. If the key is not found, it returns the default value (which is None if not specified).
    - dict.clear(): Removes all key-value pairs from the dictionary, leaving it empty.

"""

# Example of a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
# Adding a new key-value pair to the dictionary
my_dict["country"] = "USA"
print(
    my_dict
)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
# Updating an existing key-value pair
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31
# Removing a key-value pair from the dictionary
my_dict.pop("city")
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}
# Using dict.get() method
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("city", "Not Found"))  # Output: Not Found
# Using dict.keys() method
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
# Using dict.values() method
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'USA'])
# Using dict.items() method
print(
    my_dict.items()
)  # Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')])
# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Example of a nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25},
}
print(nested_dict["person1"]["name"])  # Output: Alice

# Iterate the Dictonary using for loop and get key and value
for key, value in nested_dict.items():
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: person1, Value: {'name': 'Alice', 'age': 30}
# Key: person2, Value: {'name': 'Bob', 'age': 25}

# Iterate nested dictionary
for person, details in nested_dict.items():
    print(f"Person: {person}")
    for key, value in details.items():
        print(f"  {key}: {value}")
# Output:
# Person: person1
#   name: Alice
#   age: 30
# Person: person2
#   name: Bob
#   age: 25

# Dictionary convert into tuples and iterate and show key and value using for loop
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
dict_to_tuple = tuple(my_dict.items())
for key, value in dict_to_tuple:
    print(f"Key: {key}, Value: {value}")
# Output:
# Key: name, Value: Alice
# Key: age, Value: 30
# Key: city, Value: New York

# show into table format
print(f"{'Key':<10} {'Value':<20}")
print(f"{'-'*10} {'-'*20}")
for key, value in my_dict.items():
    print(f"{key:<10} {str(value):<20}")

# Output:
# Key        Value
# ---------- --------------------
# name       Alice
# age        30
# city       New York

# dictionary update using dict.update() method
dict1 = {"name": "Alice", "age": 30}
dict2 = {"city": "New York", "country": "USA"}
dict1.update(dict2)
print(
    dict1
)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
