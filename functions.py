"""
1. In Python, Function is one type concept like Java.
2. Here Syntax is diff
   def add(a,b):
       return a+b
   function add(5,2)

"""


def add(a, b):
    return a + b


print("Total Value :", add(5, 2))


# Function with default value
def add(a, b=10):
    return a + b


print("Total Value :", add(5))


# Function with variable length argument
def add(*args):
    total = 0
    for i in args:
        total += i
    return total


print("Total Value :", add(5, 2, 3, 4))


# Function with keyword argument
def add(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total


print("Total Value :", add(a=5, b=2, c=3, d=4))

# Function with lambda expression
add = lambda a, b: a + b
print("Total Value :", add(5, 2))


# Function with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5 :", factorial(5))


# Function with nested function
def outer_function():
    print("Outer function called")

    def inner_function():
        return "Hello from inner function"

    return inner_function()


print(outer_function())

# Function with variable scope
x = 10  # Global variable


def my_function():
    global x  # Accessing global variable
    x += 5
    return x


print("Value of x after function call:", my_function())


# Function with docstring
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b


print(add.__doc__)


# Function with type hints
def add(a: int, b: int) -> int:
    return a + b


print("Total Value :", add(5, 2))
