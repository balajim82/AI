"""
    Important : By default python followes everthing as object. 
    Python Philosophy: "We're all consenting adults here" - access control is by convention, not enforcement.
    
    The object class is the ultimate base class in Python from which all classes inherit (either explicitly or implicitly).
    
    The below importent oops concepts should understand in python. These concept are similar to other languages like java. 
    But syntax are diff and implementation should understand.
      --> Class and it's Implementations
      --> Instance,class varibles usage
      --> Instance Method, Class method and static Methods.
      --> Property access specifiers.
      --> Property (setter/getter) patterns
    
    1. Class
        1> A class object in Python is an instance of a class. It is created when you define a
            class and can be used to create instances of that class.
        2>  A class object contains attributes and methods that are defined in the class.
        3>  You can create a class object in Python by defining a class using the `class` keyword and then instantiating it.
            For example:
                ```python
                class Employee:
                     # Below are Class varibles (Shared Across Instances)
                     company_name ="GenAI"
                     employee_count=0
                    def __init__(self, name, salary):
                        # Instance variables (unique to each instance)
                        self.name = name
                        self.salary=salary
                        self._department = None  # Protected (convention)
                        self.__ssn = None  # Private (name mangling)
                        # Class varible. when ever instance access then we are incrementing
                        Employee.employee_count += 1 

                    def get_details(self):
                        return f"{self.name} earns ${self.salary}"
                        
                    
            With above Example, 
             1.Class name can be "Camel" case. 
             2."__init__" This method treats as default constructor class and this is python follows syntax.
             3. self -->this nothing but "this" object in java. 
             4. "company_name" and "employee_count" are class varibles and access for all instances.
             5. "get_details"  this my own method.
    2. Object
        1. Instance of the class called "Object"
           Ex: my_employee = Employee("Balaji.M",20000)
    
    3. Access Specifiers (Public, Protected, public) 
        1. In python, By default everything treat as public.
        2. In Python, encapsulation is achieved through the use of access modifiers (public, protected, and private) to control the visibility of class attributes and methods.
            -- Public: Attributes and methods that are accessible from anywhere (no special syntax needed).
            -- Protected: Attributes and methods that are intended to be accessed only within the class and its
            -- private: Attributes and methods that are intended to be accessed only within the class itself (indicated by a double underscore prefix).
        3. To Define varible or methods as private or public or protected we can use the following syntax:
            -- Public: No special syntax needed (e.g., myVar, myMethod()).
            -- Protected: Prefix the name with a single underscore (e.g., _myVar, _myMethod()).
            -- Private: Prefix the name with a double underscore (e.g., __myVar, __myMethod()).
     4. Class varible and Instance Varible diff.
        --> It's a global varible to that class. If create any no of instances to that class but varible access the latest value.
        --> Instance varible belongs part of that Object. Can't expose this varible to across instances.
     5. Name Mangling and Access Control
        --> Generally if we delcare the varible or method as private then we can't access from out side of the class.
           In python, we can do with work around but it's not suggestble.
            # Name mangling - Python transforms __pin to _BankAccount__pin
            print(account._BankAccount__pin)  # "1234" - accessible but discouraged (Example Provided below.)
     6. Instance, Class, and Static Methods
         Instance method :
            class Circle:
                def __init__(self, radius):
                    self.radius = radius

                def area(self):  # Instance method
                    return 3.14159 * self.radius ** 2

                def circumference(self): # Instance method
                    return 2 * 3.14159 * self.radius

                circle = Circle(5)
                print(circle.area())  # 78.53975  
          Class Methods:
           Operate on class data, receive class as first argument.
           class Employee:
                employee_count = 0 # class level variable
                raise_amount = 1.04 # class level variable

                def __init__(self, name, salary):
                    self.name = name
                    self.salary = salary
                    Employee.employee_count += 1


                @classmethod
                def set_raise_amount(cls, amount):
                    # Class method - modifies class variable
                    cls.raise_amount = amount

                @classmethod
                def from_string(cls, emp_string):
                    # Alternative constructor - factory method
                    name, salary = emp_string.split('-')
                    return cls(name, int(salary))

                def apply_raise(self):
                    self.salary = int(self.salary * self.raise_amount)
          Static Methods
            Don't access instance or class data. Utility functions.
             import datetime

                class DateUtils:
                    @staticmethod
                    def is_workday(day):
                        #Static method - doesn't need instance or class
                        return day.weekday() < 5

                    @staticmethod
                    def parse_date(date_string):
                        return datetime.datetime.strptime(date_string, "%Y-%m-%d")
                        
        7. Rule of Thumb:
            Instance method: Needs self (instance data)
            Class method: Needs cls (class data) or alternative constructors
            Static method: Needs neither, pure utility function
            
        8.  Properties and Descriptors
            Case - 1 : Creating multiple setter/getter for each variable (check below Example)
            Case - 2 : Property Factory Pattern
                       The Problem with case-1: Code Repetition Imagine you have a class where multiple attributes need the exact same validation 
                       (e.g., ensuring a price or quantity is never negative). 
                       Writing individual getters and setters for each would be tedious:
                       
            The Property Factory Pattern in Python is a technique used to generate properties dynamically. 
            It is essentially a function that returns a property object, allowing you to reuse the same getter, setter, and deleter logic across multiple attributes without duplicating code.
            This pattern leverages closures—the factory function takes arguments (like the name of the attribute) and returns a property that "remembers" those arguments.
        
        9. Can a class object be used as a function in Python?
            No, a class object cannot be used as a function in Python. However, you can define a `__call__` method in the class, which allows instances of the class to be called as if they were functions.
            For example:
                ```python
                class MyClass:
                    def __call__(self):
                        print("Instance called as a function")
                my_object = MyClass()
                my_object()  # This will call the __call__ method

"""
# Basic Class Example
class Employee:
    # Class variable (shared across all instances)
    company = "XYZ"
    employee_count = 0

    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        self._department = None  # Protected (convention)
        self.__ssn = None  # Private (name mangling)

        Employee.employee_count += 1

    def get_details(self):
        return f"{self.name} earns ${self.salary}"
    
emp1 = Employee("Raaj", 120000)
emp2 = Employee("Alice", 110000)

print("Empoyee Count",Employee.employee_count)  # 2
print(emp1.company) # XYZ
print(Employee.company) # XYZ
print(emp1.get_details())  # Raaj earns $120000

# Class varible and Instance Varible Diff

class Product:
    discount = 0.1  # Class variable

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * (1 - Product.discount)
        #return self.discount

# Create instances
p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 50)

print(p1.get_discounted_price())  # 900.0
print(p2.get_discounted_price())  # 45.0

# Change class variable - affects all instances
Product.discount = 0.2
print(p1.get_discounted_price())  # 800.0
print(p2.get_discounted_price())  # 40.0

# Change instance variable - affects only that instance
p1.discount = 0.5 # changing the value 
# get_discounted_price if change to self.discount then will effect for that p1 object.
print(p1.get_discounted_price())  # 500.0
print(p2.get_discounted_price())  # 40.0

# Check what happened  
# This Entire object want to convert dict. then use this below method.
print(p1.__dict__)  # {'name': 'Laptop', 'price': 1000, 'discount': 0.5}
print(p2.__dict__)  # {'name': 'Mouse', 'price': 50}
print(Product.__dict__)  # Contains 'discount': 0.2


# Acesss specificiers checks
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public
        self._balance = balance  # Protected (convention only)
        self.__pin = "1234"  # Private (name mangling)

    def get_balance(self):
        return self._balance

    def __validate_pin(self, pin):  # Private method
        return pin == self.__pin

# Usage
account = BankAccount("ACC001", 10000)

print(account.account_number)  # Works - public
print(account._balance)  # Works - convention, not enforced
#print(account.__pin)  # AttributeError -- Private Varible -Can'taccess throw error

# Name mangling - Python transforms __pin to _BankAccount__pin
print(account._BankAccount__pin)  # "1234" - accessible but discouraged

 # AttributeError -- Method accessing. But fails due to private method.
# account.__validate_pin("1234") 

# Instance methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Instance method
        return 3.14159 * self.radius ** 2

    def circumference(self): # Instance method
        return 2 * 3.14159 * self.radius

circle = Circle(5)
print(circle.area())  # 78.53975  
print(circle.circumference())  # 31.4159 

# Class Methods
class Employee:
    employee_count = 0 # class level variable
    raise_amount = 1.04 # class level variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1


    @classmethod
    def set_raise_amount(cls, amount):
        """Class method - modifies class variable"""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        """Alternative constructor - factory method"""
        name, salary = emp_string.split('-')
        return cls(name, int(salary))

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        

# Usage
emp1 = Employee("Raaj", 100000)
emp2 = Employee("Alice", 90000)

# Class method to modify class variable
Employee.set_raise_amount(1.05)

# Alternative constructor
emp3 = Employee.from_string("Bob-95000")
print(emp3.name, emp3.salary)  # Bob 95000

# Apply raise
emp1.apply_raise()
print(emp1.salary)  # 105000

# Static Methods

import datetime

class DateUtils:
    @staticmethod
    def is_workday(day):
        """Static method - doesn't need instance or class"""
        return day.weekday() < 5

    @staticmethod
    def parse_date(date_string):
        return datetime.datetime.strptime(date_string, "%Y-%m-%d")

    @classmethod
    def get_current_year(cls):
        """Class method when you might need cls in future"""
        return datetime.datetime.now().year

# Usage - can be called without instantiation
today = datetime.date.today()
print(DateUtils.is_workday(today))  # True/False

date = DateUtils.parse_date("2025-12-17")
print(DateUtils.get_current_year())  # 2025


# Case-1 Setter/getter for varibles
class Product:
    def __init__(self, price, weight):
        self._price = price
        self._weight = weight

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0: raise ValueError("Cannot be negative")
        self._price = value

    # Now you'd have to repeat all that logic for 'weight'...
    # Like that should repeat all properties. and tedious job.
    
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0: raise ValueError("Cannot be negative")
        self._weight = value
        

#The Solution: The Property Factory
#Instead of repeating yourself, you create a function that builds the property for you

# 1. Define the Factory
# The factory function creates the local getter and setter functions and returns a property object.

def quantity_factory(storage_name):
    def getter(self):
        # instance is the 'self' of the class using the property
        return getattr(self, storage_name)

    def setter(self, value):
        if value < 0:
            raise ValueError(f"{storage_name} must be positive")
        setattr(self, storage_name, value)

    return property(getter, setter)

# 2. Use the Factory in a Class
# You assign the result of the factory to class-level attributes.

class Product:
    # We define the public name and the internal storage name
    price = quantity_factory('_price')
    weight = quantity_factory('_weight')

    def __init__(self, price, weight):
        self.price = price  # This triggers the factory setter
        self.weight = weight
    
product = Product(2000,20)
product.price = 4000


# Descriptors - Advanced Property Control
# While a property factory is a function that returns a property, a Descriptor is a dedicated class that implements the Descriptor Protocol (get, set, and delete).

class ValidQuantity:

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value


    def __set_name__(self, owner, name):
        # This is called automatically when the class is defined.
        # It lets us know the name of the variable (e.g., "price")
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, objtype=None):
        # Triggered when you do: product.price
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        # Triggered when you do: product.price = 100
        if value < 0:
            raise ValueError(f"{self.public_name} must be positive")

        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.public_name} must be >= {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.public_name} must be <= {self.max_value}")
        setattr(instance, self.private_name, value)
        
# Now, using it is incredibly clean:
class Product:
    price = ValidQuantity(min_value=0)   # No need to pass '_price' anymore!
    weight = ValidQuantity(min_value=0, max_value=10000)

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

product = Product("Laptop", 1000, 10000)
print(product.price)
print(product.weight)


# Define a __call__ method in the class
class MyCallableClass:
    def __call__(self):
        print("Instance called as a function")


my_callable_object = MyCallableClass()
my_callable_object()  # This will call the __call__ method
