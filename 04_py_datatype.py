"""
 Data Types in Python:
  --> Fundamental or primitive Data Types:
            1. int   --> 10
            2. float --> 10.2
            3. string  --> "balaji" ,'balaji'
            4. boolean  --> False or True
            5. complex  --> 10+2j
            6. none   --> Nothing but Null
  --> Derived or object Data Types:
        1. list  --> [] in java we have arraylist
        2. tuple --> () in java we have arraylist
        3. set   --> {} in java we have hashset
        4. dictionary --> {} (key-value pairs) in Java we have map
        5. frozenset --> () in java we have hashset
        6. range () in java we have range
        7. none in java we have null
        8. bytes
        9. bytesarray

1. In python, data types are used to define the type of data that a variable can hold.
2. Each data type has its own characteristics and operations that can be performed on it.
3. In python no need to  explicty define what is the data type of a variable.
4. it is determined automatically based on the value assigned to it.
   This is known as dynamic typing.
   For example, if you assign an integer value to a variable,
      it will be of type int, and if you assign a string value to a variable,
      it will be of type str.
5. in python , we can also convert one data type to another using type casting. For example, we can convert an integer to a float using the float() function, or we can convert a string to an integer using the int() function.
  int to float: float(5) -> 5.0
  float to int: int(5.7) -> 5
  string to int: int("10") -> 10
  string to float: float("3.14") -> 3.14
6. By Default all datatypes will be false.
   Like if define any datatype and print it will show false.

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

x = eval(input("Enter Value : "))
print("x value type", x)

# Converting data types.
x = int(12.3)
print(x)
print(type(x))

y = str((1, 2, 3))
print(y)
print(type(y))
