"""
This File we are going to learn about the basics of python programming
 language. We will cover the following topics:
  1. Introduction to Python
      0. python invented by Guido van Rossum in 1991
      1. Pyhon is a high level programming language
      2. Python is an interpreted language and written in C language
      3. Python is a dynamically typed language
      4. Python is a garbage collected language
      5. Python is a multi-paradigm language
      6. Python is a cross-platform language
      7. Python suppoort object-oriented programming,
         procedural programming and functional programming
      8. Python used for Gaming, Desktop applications, Web development, Data Science, Machine Learning,
         Artificial Intelligence, etc.
         Mainly for Web development, Data Science, Machine Learning and Artificial Intelligence.
      9. python is  better than other programming languages in terms of simplicity, readability and ease of use.
      10. python has a large community and a lot of libraries and frameworks which makes it easier to develop applications.
      11. In python everthing as Object internally.

  1. Comments
  2. Print
  3. PP print
  4. Keywords
  5. eval
  6. Input
  7. types of data
  9. dir
  10.help
  11. import and from

"""

# 1. Comments

""" 
Two types of comments in python:
1. Single line comment: starts with # and ends with the end of the line
2. Multi line comment: starts with ''' and ends with ''' or """ """ 
"""
# 2. Print
print("Hello World")  # This is a single line comment
print(5)  # This is a single line comment
a = 10
print("The value of a is: ", a)  # This is a single line comment
print("The value of a is: " + str(a))  # This is a single line comment
# This kind of string is called f-string and it is used to format the string.Its available in python 3.6 and above
print(f"The value of a is: {a}")

# 3. PP print
# PP print is a pretty print function which is used to print the data in a more readable format.
# It is available in the pprint module.
from pprint import pprint

data = {"name": "John", "age": 30, "city": "New York"}
print("This is Normal Print:", data)
pprint(data)

# keyword
# This keword used for see what keyword list availble in python.
import keyword

print(keyword.kwlist)

# eval() and input
# this is generally used for when ever user input gives values it will convert into auto data type.
x = eval(input("Enter product value :"))
print("Product Value entered by user", x)

# type of data
print(type(x))
y = {"name": "balaji"}
print(type(y))

# dir is for decide what type of functions can use it.
xx = 122
print(dir(xx))

# Import.
# Import used for load any Files from thirparty and with in other Modules.
import pandas
