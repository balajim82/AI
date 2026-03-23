"""
1. what is Iterator?
    An object that allows you to traverse through a sequence, one element at a time. Key Methods:
    iter() - Returns the iterator object
    next() - Returns the next item
2. What is a Generator?
   A special type of iterator that generates values on-the-fly using yield keyword.
   Benefits:
    Memory efficient (doesn't store all values)
    Lazy evaluation (generates values when needed)
    Simpler syntax than iterators
    Generator Function - Uses yield instead of return
3. When to Use Iterator and generator?
    Use Iterators when:
    You need complex stateful iteration logic
    You want full control over iteration behavior
    You're building a custom data structure

    Use Generators when:
    Processing large files or datasets
    You need memory efficiency
    Creating sequences on-the-fly
    Pipeline processing
    Infinite sequences
"""

# Iterator usage and samples
my_list = [1, 2, 3]
iterator = iter(my_list)
print(type(my_list))
print(type(iterator))

# Calling next function
# print(next(iterator))  # 1
# print(next(iterator))  # 2
# print(next(iterator))  # 3
# print(next(iterator))  # StopIteration Error

# Looping the iterator
for item in iterator:
    print(item)

my_list = [1, 2, 3, 4]
print(dir(my_list))

# Creating custom Iterator and usefull in interviews


class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


counter = Counter(1, 5)
for num in counter:
    print(num)

counter = Counter(1, 10000)
print(next(counter))


# Generator Function - Uses yield instead of return
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))
print(next(counter))


for num in count_up_to(5):
    print(num)


# Generator vs Regular Function
# Regular Function - Load all data once.
def get_numbers(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result  # Returns all at once


numbers = get_numbers(1000000)  # All stored in memory!
print(type(numbers))
numv = len(numbers)
print(numv)


# Using generator function -yield keword used.
def get_numbers(n):
    for i in range(1, n + 1):
        yield i  # Returns one at a time


numbers = get_numbers(1000000)  # Only one number in memory at a time!
print(type(numbers))
numbers

# Generator Expressions

# List comprehension (creates entire list in memory)
squares_list = [x**2 for x in range(10)]
print(type(squares_list))

# Generator expression (creates values on demand)
squares_gen = (x**2 for x in range(10))
print(type(squares_gen))

for square in squares_gen:
    print(square)

# Performance Comparison (Iter and Generator)
import sys

# List (stores all in memory)
list_nums = [x for x in range(10000)]
print(type(list_nums))
print(sys.getsizeof(list_nums))  # ~85 KB

# Generator (stores only one at a time)
gen_nums = (x for x in range(10000))
print(type(gen_nums))
print(sys.getsizeof(gen_nums))  # ~128 bytes


def generator1():
    yield 1
    yield 2


def generator2():
    yield 3
    yield 4


def combined():
    yield from generator1()
    yield from generator2()


# Usage
for num in combined():
    print(num)

# Trying to reuse exhausted generator
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # [] (empty - already exhausted)

# Using generator when you need random access
gen = (x for x in range(10))
# gen[5]  # Error! Generators don't support indexing

# Convert to list if you need multiple passes:
gen = (x for x in range(10))
data = list(gen)  # Now you can access data[5]
print(data)
