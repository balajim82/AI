"""
  Magic Methods -- There are some frequently used and prebuilt functions using third party Lib.
  
  The object class is the ultimate base class in Python from which all classes inherit (either explicitly or implicitly).
  
  
  
  
  
    
    
"""

# These are equivalent in Python 3
class MyClass:
    pass

class MyClass(object):  # Explicit inheritance
    pass

# Both inherit from object
print(MyClass.__bases__)  # (<class 'object'>,)
print(isinstance(MyClass(), object))  # True

dir(object)

# Format
class Vector:
    def __init__(self, x, y):
        """Constructor"""
        self.x = x
        self.y = y

    def __repr__(self):
        """Developer-friendly representation"""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """User-friendly representation"""
        return f"<{self.x}, {self.y}>"

    def __format__(self, format_spec):
        """Custom formatting"""
        if format_spec == 'polar':
            import math
            mag = math.sqrt(self.x**2 + self.y**2)
            angle = math.atan2(self.y, self.x)
            return f"({mag:.2f}, {angle:.2f})"
        return str(self)
    
v = Vector(3, 4)
print(repr(v))  # Vector(3, 4)
print(str(v))   # <3, 4>
print(f"{v:polar}")  # (5.00, 0.93)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# print(p1 - p2) Here wont work. Using below method can perform

#Arithmetic Operators - Operator Overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """v * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """scalar * v (reversed)"""
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        """v / scalar"""
        return Vector(self.x / scalar, self.y / scalar)

    def __abs__(self):
        """abs(v) - magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __neg__(self):
        """-v"""
        return Vector(-self.x, -self.y)

    def __eq__(self, other):
        """v1 == v2"""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)  # Vector(6, 8)
print(v1 - v2)  # Vector(-2, -2)
print(v1 * 3)   # Vector(6, 9)
print(3 * v1)   # Vector(6, 9) - uses __rmul__
print(v1 / 2)   # Vector(1.0, 1.5)
print(abs(v1))  # 3.605551275463989
print(-v1)      # Vector(-2, -3)
print(v1 == Vector(2, 3))  # True

#Comparison Operators
# The @total_ordering decorator is a class decorator from functools that automatically generates missing comparison methods (lt, le, gt, ge) if you define eq and one other comparison method.

from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        """You MUST define __eq__"""
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch) #compare mutiple items using tuple

    def __lt__(self, other):
        """Define just ONE comparison method"""
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

    # __le__, __gt__, __ge__ are AUTO-GENERATED!
    
    # Usage
v1 = Version(1, 2, 3)
v2 = Version(1, 3, 0)

print(v1 < v2)   # True  (defined by you)
print(v1 > v2)   # False (generated automatically)
print(v1 <= v2)  # True  (generated automatically)
print(v1 >= v2)  # False (generated automatically)
print(v1 == v2)  # False (defined by you)

#Basic Tuple Comparison - Tuples are compared lexicographically (element by element from left to right) in Python.

# Tuples are compared element by element
(1, 2, 3) < (1, 2, 4)    # True  (3 < 4)
(1, 2, 3) < (1, 3, 0)    # True  (2 < 3, doesn't check 3rd element)
(2, 0, 0) > (1, 9, 9)    # True  (2 > 1, doesn't check rest)

# Equal comparison
(1, 2, 3) == (1, 2, 3)   # True
(1, 2, 3) != (1, 2, 4)   # True

# All comparison operators work
(1, 2) <= (1, 2)         # True
(1, 2) >= (1, 1)         # True

#Container Methods
# In Python, "container methods" refer to the special methods (often called "dunder" or magic methods) that allow an object to behave like a container, which is an object that holds other objects. The core functionality of a container is the ability to perform a membership test using the in keyword.

class MyList:
    def __init__(self):
        self._items = []

    def __len__(self):
        """len(my_list)"""
        return len(self._items)

    def __getitem__(self, index):
        """my_list[0]"""
        return self._items[index]

    def __setitem__(self, index, value):
        """my_list[0] = 'new value'"""
        self._items[index] = value

    def __delitem__(self, index):
        """del my_list[0]"""
        del self._items[index]

    def __contains__(self, item):
        """'item' in my_list"""
        return item in self._items

    def __iter__(self):
        """for item in my_list"""
        return iter(self._items)

    def append(self, item):
        self._items.append(item)
        
my_list = MyList()
my_list.append("hello")
my_list.append("world")

print(len(my_list))           # 2 (__len__)
print(my_list[0])             # "hello" (__getitem__)
my_list[0] = "hi"             # (__setitem__)
print("hi" in my_list)        # True (__contains__)

for item in my_list:          # (__iter__)
    print(item)

del my_list[0]                # (__delitem__)

#Dataclasses
# The @dataclass decorator (introduced in Python 3.7) is essentially a boilerplate generator. It’s designed for classes that primarily exist to store data, automatically writing the "boring" parts of the code for you—like the constructor, the string representation, and equality checks.
# The "Boilerplate" Problem

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r}, email={self.email!r})"

    def __eq__(self, other):
        if not isinstance(other, User): return False
        return (self.name, self.age, self.email) == (other.name, other.age, other.email)
    
# The Dataclass Solution

# With @dataclass, all that logic is compressed into a few lines. You simply define the attributes with type hints, and Python handles the rest.

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

# Use it immediately
user1 = User("Alice", 30, "alice@example.com")
print(user1)  # Output: User(name='Alice', age=30, email='alice@example.com')
# user2 = User("jhon", 30) -- it will fail. Exact params should pass here.

from dataclasses import dataclass, field
from typing import List

@dataclass
class Employee:
    """Automatically generates __init__, __repr__, __eq__"""
    name: str
    salary: float
    department: str = "Engineering"  # Default value
    skills: List[str] = field(default_factory=list)  # Mutable default

    def __post_init__(self):
        """Called after __init__"""
        if self.salary < 0:
            raise ValueError("Salary must be positive")

# What does it generate automatically?
# When you apply the decorator, it inspects your type hints and adds these methods:
# init: A constructor that assigns arguments to attributes.
# repr: A nice, readable string representation (instead of <__main__.User object at 0x... >).
# eq: Allows you to compare two objects (e.g., user1 == user2) based on their values, not their memory address.

# Usage
emp1 = Employee("Raaj", 120000)
emp2 = Employee("Alice", 110000, "Marketing", ["SEO", "Content"])

print(emp1)  # Employee(name='Raaj', salary=120000, department='Engineering', skills=[])
print(emp1 == Employee("Raaj", 120000))  # True

# Modify
emp1.skills.append("Python")

#Dataclass Options

from dataclasses import dataclass, field

@dataclass(
    frozen=True,  # Immutable
    order=True,   # Generates comparison methods
    slots=True    # Use __slots__ for memory efficiency
)
class Point:
    x: float
    y: float = field(repr=False)  # Exclude from repr
    z: float = field(default=0, compare=False)  # Don't use in comparisons
    
p1 = Point(1.0, 2.0, 3.0)
p2 = Point(1.0, 5.0, 6.0)

# Frozen - immutable
# p1.x = 10  # FrozenInstanceError

# Order - can compare
print(p1 < p2)  # Compares x and y (not z)

# Repr
print(p1)  # Point(x=1.0, z=3.0) - no y

# how to define class variable within a @dataclass
# To define a class variable within a @dataclass, you must use the typing.ClassVar annotation. This tells the dataclass decorator to exclude the variable from the auto-generated init, repr, eq, and other methods, ensuring it remains a true class-level attribute shared by all instances.


from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1

    # Class variable - not instance variable
    tax_rate: ClassVar[float] = 0.1

    # Computed field
    total: float = field(init=False)

    def __post_init__(self):
        self.total = self.price * self.quantity * (1 + self.tax_rate)
        
product = Product("Laptop", 1000, 2)
print(product.total)  # 2200.0

# Convert to dict/tuple
print(asdict(product))  # {'name': 'Laptop', 'price': 1000, 'quantity': 2, 'total': 2200.0}
print(astuple(product))  # ('Laptop', 1000, 2, 2200.0)

#NamedTuples - Immutable Data Classes
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    z: float = 0  # Default value

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

p = Point(3, 4, 0)
print(p.x, p.y)  # 3 4
print(p[0], p[1])  # 3 4 (also tuple-like)
print(p.magnitude())  # 5.0

# Immutable
# p.x = 10  # AttributeError

# Unpacking
x, y, z = p

# Convert to dict
print(p._asdict())  # {'x': 3, 'y': 4, 'z': 0}

# Replace (creates new instance)
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=4, z=0)


# Dataclass vs NamedTuple vs Regular Class

# Regular class
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# NamedTuple
from typing import NamedTuple
class TuplePoint(NamedTuple):
    x: float
    y: float

# Dataclass
from dataclasses import dataclass
@dataclass
class DataPoint:
    x: float
    y: float

# Comparison
import sys

regular = RegularPoint(1, 2)
tuple_point = TuplePoint(1, 2)
data_point = DataPoint(1, 2)

# Memory
print(sys.getsizeof(regular))      # 48 bytes
print(sys.getsizeof(tuple_point))  # 40 bytes
print(sys.getsizeof(data_point))   # 48 bytes

# Mutability
regular.x = 10  # OK
# tuple_point.x = 10  # Error - immutable
data_point.x = 10  # OK

# When to use what:
# Regular class: Need full control, complex behavior
# NamedTuple: Immutable data, tuple-like behavior
# Dataclass: Mutable data, less boilerplate