"""
1. In Python, Function is one type concept like Java.
    Function definition
    def func_name(param1, param2, param3):
        stat1
        stat2
        stat3
        stat4
        return stat
    Functin definition is not function execution
   Ex:
        def add(a,b):
            return a+b
        function add(5,2)
2. There diff types function defination can declare it.
   Ex1:  def emp_info(ename, eid, esal):   ---> Here Not specified what type of datatype
            print(ename)
            print(eid)
            print(esal)
         return 200
    Below specified what type of datatype and return type as well. In industry stardards below
     one uses widely.
   Ex2: def emp_info(ename:str, eid:int, esal:str)-> int:
            print(ename)
            print(eid)
            print(esal)
        return 2000
   --> Fourth Param assigned default value. While calling function if dont pass value
       it will consider this default. if pass value it will overide and takes latest value.
   Ex3 : def emp_info(ename, eid, esal, eaddr = 'BLR'):
            print(ename)
            print(eid)
            print(esal)
            print(eaddr)

      The below one more type of function def. Here *args can accept tuple
       and **kwargs treat as dictionry.
       These two always should be last params of the function defination.
      # Variable length arguments - *args - tuple
      # Variable length keyworded arguments - **kwargs - dictionary

   Ex4:   def emp_info(ename, eid, esal, *var, **kwvar):
            print(ename)
            print(eid)
            print(esal)
            #print(var, type(var))
            print(kwvar, type(kwvar))

      emp_info('ABC', 101, 10000, 'ABC Street', 'ABC Locality','Bangalore', State = 'Karnataka', Country = 'INdia', Pin = 560000)

   Function with lambdda
   # Anonymous Functions - Function without name - lambda
   # lambda var:expr
   Ex:  f = lambda x : x **2
        f(6)

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

print("lambd exp: ", (lambda x: x**2)(2))

lst = [(9, 4), (4, 1), (3, 5), (6, 9), (1, 2), (4, 3)]


def my_fun(tpl):
    return tpl[-1]


print(my_fun(lst))

lst.sort(key=lambda tpl: tpl[-1])
print(lst)

# Gloabal Function
print("Globale Function: ", sorted(lst))

dct = {1: 20, 20: 200, 3: 3}
print(
    "Dict sorted using lambda and sorted ",
    sorted(dct.items(), key=lambda item: item[-1]),
)


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


def emp_info(ename, eid, esal, *var, **kwvar):
    print(ename)
    print(eid)
    print(esal)
    # print(var, type(var))
    print(kwvar, type(kwvar))


emp_info(
    "ABC",
    101,
    10000,
    "ABC Street",
    "ABC Locality",
    "Bangalore",
    State="Karnataka",
    Country="INdia",
    Pin=560000,
)

# filter(func, seq)
# returns filter object - based on function return value it will filter a seq
# resultant seq will be shortenend

lst = list(range(10, 21))
print("Original list : ", (lst))
newlist = list(filter(lambda num: num % 2 == 0, lst))
print("Filtered list : ", (newlist))


# map(func, seq)
# return map object - when we want to map every element of a seq with somw values

lst = [2, 3, 5, 6, 7, 8]
maplist = list(map(lambda num: num**2, lst))

print("Map List :", maplist)


# reduce(func, seq) - aggregate - sum, prod, max, min
from functools import reduce

lst = list(range(10, 21))


print(reduce(lambda x, y: x * y, lst))


from functools import reduce

numbers = [1, 2, 3, 4, 5]
# Starts with 0 + 1, then adds 2, then 3, and so on.
sum_with_start = reduce(lambda x, y: x + y, numbers, 0)
print(sum_with_start)
# Starts with 10 + 1, then adds 2, then 3, and so on.
sum_with_start10 = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_start10)
