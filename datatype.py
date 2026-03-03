"""
 Data Types in Python:
  primitive Data Types:
  1. int
  2. float
  3.string
  4. boolean
  5. complex
object Data Types:
1. list  [] in java we have arraylist
2. tuple () in java we have arraylist
3. set   {} in java we have hashset
4. dictionary {} (key-value pairs) in Java we have map
5. frozenset () in java we have hashset
6. range () in java we have range
7. none in java we have null

In python, data types are used to define the type of data that a variable can hold. Each data type has its own characteristics and operations that can be performed on it.

In python no need to  explicty define what is the data type of a variable,
it is determined automatically based on the value assigned to it. This is known as dynamic typing. For example, if you assign an integer value to a variable, it will be of type int, and if you assign a string value to a variable, it will be of type str.

in python , we can also convert one data type to another using type casting. For example, we can convert an integer to a float using the float() function, or we can convert a string to an integer using the int() function.
  int to float: float(5) -> 5.0
  float to int: int(5.7) -> 5
  string to int: int("10") -> 10
  string to float: float("3.14") -> 3.14
"""

a = 10
print(type(a))  # <class 'int'>
b = 10.5
print(type(b))  # <class 'float'>
c = "Hello"
print(type(c))  # <class 'str'>
d = True
print(type(d))  # <class 'bool'>
e = 1 + 2j
print(type(e))  # <class 'complex'>
f = [1, 2, 3]
print(type(f))  # <class 'list'>
g = (1, 2, 3)
print(type(g))  # <class 'tuple'>
h = {1, 2, 3}
print(type(h))  # <class 'set'>
i = {"name": "Alice", "age": 30}
print(type(i))  # <class 'dict'>
j = frozenset([1, 2, 3])
print(type(j))  # <class 'frozenset'>
k = range(5)
print(type(k))  # <class 'range'>
l = None
print(type(l))  # <class 'NoneType'>
