"""
Control statements are used to control the flow of execution in a program. They allow you to make decisions, repeat actions, and manage the flow of your code based on certain conditions.
  Conditionl statements include :
  1. If statements: Used to execute a block of code if a specified condition is true.
  2. Else statements: Used in conjunction with if statements to execute a block of code if the condition is false.
  3. Elif statements: Used to check multiple conditions after an initial if statement.
  4. nested if statements: Used to check multiple conditions within another if statement.
  For loops include:
  1. While loops: Used to repeatedly execute a block of code as long as a specified condition is true.
  2. Do-while loops: Similar to while loops, but the block of code is executed at least once before the condition is tested.
  3. For loops: Used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.
  4. Nested loops: Used to have one loop inside another loop, allowing for more complex iterations.
  Jump statements include:
  1. Break: Used to exit a loop prematurely when a certain condition is met.
  2. Continue: Used to skip the current iteration of a loop and move to the next iteration.
  3. Pass: Used as a placeholder for code that will be implemented later, allowing the program to run without errors.

"""

# Example of if statement
x = 10
if x > 5:
    print("x is greater than 5")
# Example of else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")
# Example of elif statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is less than or equal to 5")
# Example of nested if statement
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")
    else:
        print("a is greater than or equal to 20")
else:
    print("a is less than or equal to 10")

# Example of while loop
i = 0
while i < 5:
    print(i)
    i += 1
# nested while loop
j = 0
while j < 3:
    k = 0
    while k < 2:
        print(f"j: {j}, k: {k}")
        k += 1
    j += 1
# Example of for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Example of break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Example of continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

a = "Balaji is great"
for k in a:
    if k == "g":
        continue
    print(k)


# Example of pass statement
def my_function():
    pass  # This function does nothing for now


my_function()  # Calling the function, it will not do anything
