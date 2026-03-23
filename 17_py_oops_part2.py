"""
   Here below topic going to discuss.
   --> Inheritence 
   --> Abstraction  (Abstract Class)
   --> PolyMorphisum 
   
1.  # Inheritance in Python:
    1. Inheritance is a fundamental object-oriented programming (OOP) concept that allows a new class (called a child or subclass) to inherit attributes and behaviors (methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
    2. The child class can also have its own unique attributes and methods, in addition to those inherited from the parent class.
    This allows for the creation of more specific classes based on general ones, facilitating code organization and maintenance.
    3. Inheritance supports the concept of "is-a" relationship, where the child class is a specialized version of the parent class.
    For example, if we have a parent class "Animal," a child class "Dog" can inherit from it, indicating that a dog is an animal.
    3. Types of Inheritance in Python:
    1. Single Inheritance: A child class inherits from a single parent class.
        Example : parent class : Father, child class : Son
    2. Multiple Inheritance: A child class inherits from multiple parent classes.
        Note:- In other programming languages, multiple inheritance can lead to ambiguity (known as the "diamond problem"),
        but Python uses a method resolution order (MRO) to handle this issue effectively.
        Ex: parent class 1 : Father, parent class 2 : Mother, child class : Son
    3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
            Ex: parent class 1 : Grandfather, parent class 2 : Father, child class : Son
    4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
        Ex: parent class : Father, child class 1 : Son, child class 2 : Daughter
    5. Hybrid Inheritance: A combination of two or more types of inheritance.

 -- Imp Points : 
    1-> In Python, there is no keywords like in java -> 'extends or implements' 
    2-> In Python, the rule is: If you define init in the child class, you "hide" or "block" the parent's init. 
    Python assumes you want to take full control of the initialization process, so it won't do anything behind your back.
    3-> Constructor Chaining - init in python. 
        If the child class doesn't define its own constructor, Python will automatically look up the family tree and use the parent's constructor.
        class Animal:
                def __init__(self, name):
                    print("Parent init called")
                    self.name = name

            class Dog(Animal):
                pass # No __init__ here

            # Python looks at Animal and calls its __init__ automatically
            my_dog = Dog("Buddy")
            # Output: Parent init called
            my_dog.name
    4--> Scenario B: The Child HAS an init
         As soon as you add def init to the Dog class, the "automatic" link to the parent's constructor is broken.
         class Animal:
            def __init__(self, name):
                print("Parent init called")
                self.name = name

         class Dog(Animal):
            def __init__(self, name, breed):
                print("Child init called")
                #super().__init__(name)
                self.breed = breed
                # Python STOPPED here. It will NOT call Animal.__init__
                # unless you specifically tell it to with super(). super().__init__(name)

            my_dog = Dog("Buddy", "Labrador")
            # Output: Child init called
            print(my_dog.name) # This would crash with an AttributeError!
   2. Abstraction (Abstraction - Abstract Base Classes (ABC))
       Abstraction in Python is made up of key components like abstract methods, concrete methods, abstract properties and class instantiation rules.
   3. Polymorphsum
      1. Poly means  -- Many  Morhph means -- Forms  is means -- Process
2. In Python, Polymorphism is the ability of a function or an object to take on many forms.
    It allows us to define methods in the child class with the same name as defined in their parent class. It is one of the core concepts of Object-Oriented Programming (OOP) and is used to perform a single action in different ways.
3. Polymorphism can be achieved in Python through method overriding and method overloading.
4. Types of Polymorphism in Python:
    1. Method Overriding: When a child class provides a specific implementation of a method that is already defined in its parent class, it is called method overriding. The child class's method will be called instead of the parent class's method when invoked on an instance of the child class.
        Example : parent class : Father, child class : Son
    2. Method Overloading: Python does not support method overloading in the traditional sense as seen in other programming languages.
    However, we can achieve similar functionality using default arguments or variable-length arguments.
    Example : A function that can accept different numbers of arguments and behaves differently based on the number of arguments passed.
5. Polymorphism allows for code flexibility and extensibility, enabling developers to write more generic and reusable code. It promotes the concept of "one interface, multiple implementations," which is a key principle in OOP.
6.  Method Overloading in Python
        Python does not support method overloading by default. If you define multiple methods with the same name, only the latest definition will be used.    
        But we have thirdparty lib (MultiDispatch) can solve.
"""


# Example of Single Inheritance
class Father:
    def __init__(fself, father_name):
        fself.father_name = father_name

    def display(fself):
        print(f"Father's name: {fself.father_name}")


class Son(Father):
    def __init__(self, son_name, father_name):
        super().__init__(father_name)
        self.son_name = son_name

    def display(self):
        print(f"Son's name: {self.son_name}")
        super().display()

# Create an instance of the Son class
son = Son("John", "Michael")
son.display()

# Sample and Simple Inheritence.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement")

    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching"

dog = Dog("Buddy", "Labrador")
print(dog.speak())  # Buddy says Woof!
print(dog.move())  # Buddy is moving (inherited)
print(dog.fetch())  # Buddy is fetching

# Check inheritance
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True


# Scenario A: The Child has NO init
class Animal:
    def __init__(self, name):
        print("Parent init called")
        self.name = name

class Dog(Animal):
    pass # No __init__ here

# Python looks at Animal and calls its __init__ automatically
my_dog = Dog("Buddy")
# Output: Parent init called
# my_dog.name

# Scenario B: The Child HAS an init
class Animal:
    def __init__(self, name):
        print("Parent init called")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        print("Child init called")
        #super().__init__(name)
        self.breed = breed
        # Python STOPPED here. It will NOT call Animal.__init__
        # unless you specifically tell it to with super(). super().__init__(name)

my_dog = Dog("Buddy", "Labrador")
# Output: Child init called
#  print(my_dog.name) # This would crash with an AttributeError!


# Example of Multiple Inheritance
class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def display_father(self):
        print(f"Father's name: {self.father_name}")


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def display_mother(self):
        print(f"Mother's name: {self.mother_name}")


class Child(Father, Mother):
    def __init__(self, child_name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def display_child(self):
        print(f"Child's name: {self.child_name}")
        self.display_father()
        self.display_mother()


# Create an instance of the Child class
child = Child("Rithvik", "Balaji.M", "Rajini.M")
child.display_child()

# Multiple Inheritance - Solving Diamond Problem with Method Resolution Order (MRO) - C3 Linearization
# Start with left only in order.
# A extends B and A extends C now D extends B and C this dimond problem
class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
        print("In Class3")

class Class4(Class2, Class3):
    pass

obj = Class4()
obj.m()

# Example 4: Calling methods of parent classes from child class
class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)

class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)

obj = Class4()
obj.m()
Class4.__mro__

# Output
# In Class4
# In Class2
# In Class1
# In Class3
# In Class1
# (__main__.Class4, __main__.Class2, __main__.Class3, __main__.Class1, object)


class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return "B -> " + super().greet()

class C(A):
    def greet(self):
        return "C -> " + super().greet()

class D(B, C):
    def greet(self):
        return "D -> " + super().greet()
        #print(super().greet())
        #return "D -> "  D -> B -> A -> C -> A

# MRO: D -> B -> C -> A -> object
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

d = D()
print(d.greet())  # D -> B -> C -> A

# Understand the flow
# 1. D.method() called -> returns "D -> " + super().method()
# 2. super() in D calls B.method() -> returns "B -> " + super().method()
# 3. super() in B calls C.method() (not A!) -> returns "C -> " + super().method()
# 4. super() in C calls A.method() -> returns "A"
# Final: "D -> B -> C -> A"

# Diamond Problem - Solved by MRO
class Base:
    def __init__(self):
        print("Base.__init__")
        self.value = "base"

class Left(Base):
    def __init__(self):
        print("Left.__init__")
        super().__init__()
        self.value = "left"

class Right(Base):
    def __init__(self):
        print("Right.__init__")
        super().__init__()
        self.value = "right"

class Bottom(Left, Right):
    def __init__(self):
        print("Bottom.__init__")
        super().__init__()
        self.value = "bottom"


# Create instance
obj = Bottom()
# Output:
# Bottom.__init__
# Left.__init__
# Right.__init__
# Base.__init__

print(obj.value)  # bottom
print(Bottom.__mro__)
# Bottom -> Left -> Right -> Base -> object

# Example of Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

    def display_grandfather(self):
        print(f"Grandfather's name: {self.grandfather_name}")


class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        super().__init__(grandfather_name)
        self.father_name = father_name

    def display_father(self):
        print(f"Father's name: {self.father_name}")
        super().display_grandfather()


class Son(Father):
    def __init__(self, son_name, father_name, grandfather_name):
        super().__init__(father_name, grandfather_name)
        self.son_name = son_name

    def display_son(self):
        print(f"Son's name: {self.son_name}")
        super().display_father()


# Create an instance of the Son class
son = Son("Rithvik", "Balaji.M", "Sudhakar.M")
son.display_son()


# Example of Hierarchical Inheritance
class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def display_father(self):
        print(f"Father's name: {self.father_name}")


class Son(Father):

    def __init__(self, son_name, father_name):
        super().__init__(father_name)
        self.son_name = son_name

    def display_son(self):
        print(f"Son's name: {self.son_name}")
        super().display_father()


class Daughter(Father):
    def __init__(self, daughter_name, father_name):
        super().__init__(father_name)
        self.daughter_name = daughter_name

    def display_daughter(self):
        print(f"Daughter's name: {self.daughter_name}")
        super().display_father()


# Create instances of the Son and Daughter classes
son = Son("Rithvik", "Balaji.M")
daughter = Daughter("Rithika", "Balaji.M")
son.display_son()
daughter.display_daughter()


# Example of Hybrid Inheritance
class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name

    def display_grandfather(self):
        print(f"Grandfather's name: {self.grandfather_name}")


class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        # avoid using super() here because in a multiple-inheritance
        # scenario (Son inherits Father and Mother) the MRO will
        # route super() to Mother.__init__, which expects a different
        # signature.  Call Grandfather.__init__ directly instead.
        Grandfather.__init__(self, grandfather_name)
        self.father_name = father_name

    def display_father(self):
        print(f"Father's name: {self.father_name}")
        super().display_grandfather()


class Mother(Grandfather):
    def __init__(self, mother_name, grandfather_name):
        # same reasoning as Father: use explicit call to avoid
        # unintended dispatch through the MRO
        Grandfather.__init__(self, grandfather_name)
        self.mother_name = mother_name

    def display_mother(self):
        print(f"Mother's name: {self.mother_name}")
        super().display_grandfather()


class Son(Father, Mother):
    def __init__(self, son_name, father_name, mother_name, grandfather_name):
        Father.__init__(self, father_name, grandfather_name)
        Mother.__init__(self, mother_name, grandfather_name)
        self.son_name = son_name

    def display_son(self):
        print(f"Son's name: {self.son_name}")
        self.display_father()
        self.display_mother()


# Create an instance of the Son class
son = Son("Rithvik", "Balaji.M", "Rajini.M", "Sudhakar.M")
son.display_son()


# Abstract Demo

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclass"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclass"""
        pass

    def describe(self):
        """Concrete method - can be inherited as-is"""
        return f"{self.__class__.__name__} with area {self.area()}"

# This will fail
# shape = Shape()  # TypeError: Can't instantiate abstract class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Usage
circle = Circle(5)
rect = Rectangle(4, 6)

print(circle.area())  # 78.53975
print(rect.describe())  # Rectangle with area 24

# Abstract Class Methods and Static Methods
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @classmethod
    @abstractmethod
    def from_file(cls, filename):
        """Abstract class method"""
        pass

    @staticmethod
    @abstractmethod
    def validate_data(data):
        """Abstract static method"""
        pass

    @abstractmethod
    def process(self):
        pass

class CSVProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_file(cls, filename):
        # Read CSV file
        data = []  # Simulate reading
        return cls(data)

    @staticmethod
    def validate_data(data):
        return isinstance(data, list)

    def process(self):
        return f"Processing {len(self.data)} rows"

# Method Overloading
class productOverload:
    def product(a, b):
        p = a * b
        print(p)

    def product(a, b, c):
        p = a * b*c
        print(p)
        
p=productOverload()
# p.product(4, 5, 5) #TypeError: productOverload.product() takes 3 positional arguments but 4 were given

# Multiple Dispatch
# Python's multipledispatch library allows true method overloading by dispatching functions based on parameter types and counts. Install multipledispatch module using the following command:

from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)

product(2, 3)
product(2, 3, 2)
product(2.2, 3.4, 2.3)