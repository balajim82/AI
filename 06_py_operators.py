"""
We are going to discuss about different type of operators in python.
   1 Arithmetic
   2 Compariosn
   3 Equality
   4 Logical
   5 Assignment
   6 Compound Assigment
   7 Membership
   8 Identity

"""

# Arithmetic - +, -, *, /(Float Division), //(Floor DIvision), %(Modulo - remainder), **(Exponent - raises the power)
num1 = 10
num2 = 3
print(num1 + num2)  # 13
print(num1 - num2)  # 7
print(num1 * num2)  # 30
print(
    num1 / num2
)  # Float Division/True division, Complete division (3.3333333333333335)
print(num1 // num2)  # Floor Division - returns a floor value of (10/3) (3)
print(num1 % num2)  # 1
print(num1**num2)  # 1000

# ceil = 4
# num = 3.9
# floor = 3

# ceil = 4
# num = 3.09
# floor = 3

# Comparison Operator - >, < , >=, <=
# Always returns Boolean Value - True, False
# Comparison using comapriosn is possible
# only between similar data types except int and float

print(10 < 100)  # True

print(10 < 100.20)  # True

# print(
#     10 < 10 + 20j
# )  # TypeError: '<' not supported between instances of 'int' and 'complex'

print(ord("A"))  # 65
print(chr(65))  # A

print(ord("A") <= 65)  # True

print("ABD" < "ABC")  # False


print(ord("A"))  # 65
print(ord("X"))  # 88

# Equality - ==, !=
# Return only boolean values
# Comparison using equality is possible between different data types

print(10 == 10)  # == always compare the content

a = 1000
b = 1000
print(a == b)  # true  # == always compare the content
print(a is b)  # False # will check Reference.

print("A" == 65)

# Logical Operator - and or not

# and Truth table - False
# True and True = True
# False and True = False
# True and False = False
# False and False = False

# or Truth table - True
# True or True = True
# False or True = True
# True or False = True
# False or False = False

# not
# not True = False
# not False = True

# (10 == 10) and (10>20)

# if A and B are some value
# result of (A and B) is A if A is False else result is B
# result of (A or B) is A if A is True else result is B


# 10 and 20

# 10 or 20


# 0 and 0.0
# 0 or 0.0

z = (10 == 10) and (10 > 20)
print(z)  # False

# Membebership Operator - in, not in --- boolean
# True, False
# Collection - Seq(String, list, Tuple), Map - (Set, Dictionary)

print("1" in "python Python 10")
# print('P' in 'python')
# print('Pyt' in 'python')
# print('pyt' in 'python')
# print('pn' in 'python')


# print(10 in [10,20,30])
# print(10 in (10,20,30))

# d = {1:100, 2:200, 3:300, 'a':'Python'}
# print(1 in d)
# print(100 in d)


# Object reusability - object can be reused
# int - -5 to 256
# string - a-z, A-Z, 0-9, _
# None, True False

# Float, complex and derived - not available

# a = 10
# b = 10
# print(id(a))
# print(id(b))


# a = 1000
# b = 1000
# print(id(a))
# print(id(b))


# Identity Operator - is, is not -
# Return Boolean Value

# a = 10
# b = 10
# print(a is b)
# print(a == b)


a = 1000
b = 1000
print(a is b)  # Will check Ref or memory location
print(a == b)  # Will check content.
