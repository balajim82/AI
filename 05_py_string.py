"""
1. String is a sequence of characters.
2. In Python, strings are immutable, meaning that once they are created, they cannot be changed.
3. However, you can perform various operations on strings to create new strings or manipulate existing ones.
4. String with single Quotes ,
  double quotes (This one used always and it supports 's ) and
  triple quotes are used to define string literals in Python.
  Triple quotes are used for multi-line strings.
5.Here are some common string operations in Python:
    1. Concatenation: You can concatenate strings using the `+` operator.
        Example: `greeting = "Hello, " + "world!"`
    2. Repetition: You can repeat a string using the `*` operator.
        Example: `echo = "Echo! " * 3`
    3. Slicing: You can extract a portion of a string using slicing.
        Example: `substring = "Hello, world!"[0:5]`  # This will give you "Hello"
    4. Length: You can get the length of a string using the `len()` function.
    5. String Methods: Python provides various built-in methods for string manipulation, such as `upper()`, `lower()`, `strip()`, `replace()`, and many more.
    6. String Formatting: You can format strings using f-strings (formatted string literals) or the `format()` method.
        Example: `name = "Alice"; greeting = f"Hello, {name}!"
    7  . Escape Characters: You can use escape characters to include special characters in strings, such as `\n` for a new line or `\t` for a tab.
        Example: `text = "Line 1\nLine 2"`
    8. String Comparison: You can compare strings using comparison operators like `==`, `!=`, `<`, `>`, etc.
        Example: `is_equal = "Hello" == "hello"`  # This will be
        False because of case sensitivity.
    9 . String Membership: You can check if a substring is present in a string using the `in` keyword.
        Example: `is_present = "world" in "Hello, world!"`  # This will be True
    10. String Splitting and Joining: You can split a string into a list of substrings using the `split()` method and join a list of strings into a single string using the `join()` method.
        Example: `words = "Hello, world!".split(", ")`  # This will give you ['Hello', 'world!']
        Example: `sentence = " ".join(["Hello", "world!"])`  # This will give you "Hello world!"
    11. String Immutability: Since strings are immutable, any operation that modifies a string will create a new string rather than changing the original one.
    12. String Indexing: You can access individual characters in a string using indexing.
        Example: `first_char = "Hello"[0]`  # This will give you 'H'
    13. String Methods: Python provides a wide range of string methods for various operations,
        such as `find()`, `count()`, `startswith()`, `endswith()`, and many more.
    14. String Formatting: You can format strings using f-strings (formatted string literals) or the `format()` method.
        Example: `name = "Alice"; greeting = f"Hello, {name}!"`  # This will give you "Hello, Alice!"
    15. String Encoding and Decoding: You can encode a string into bytes using the `encode()` method and decode bytes back into a string using the `decode()` method.
        Example: `encoded = "Hello".encode('utf-8')`  # This will give you b'Hello'
        Example: `decoded = encoded.decode('utf-8')`  # This will give you "Hello"
    16. String Case Conversion: You can convert the case of a string using methods like `upper()`, `lower()`, `capitalize()`, and `title()`.
        Example: `text = "hello world"; upper_text = text.upper()`  # This will give you "HELLO WORLD"
    17. String Stripping: You can remove leading and trailing whitespace from a string using the `strip()` method.
        Example: `text = "  Hello, world!  "; stripped_text = text.strip()`  # This will give you "Hello, world!"
    18. String Replacement: You can replace occurrences of a substring with another substring using the `replace()` method.
        Example: `text = "Hello, world!"; new_text = text.replace("world", "Python")`  # This will give you "Hello, Python!"
    19. String Alignment: You can align strings using methods like `ljust()`, `rjust()`, and `center()`.
        Example: `text = "Hello"; aligned_text = text.center(10)`  # This will give you "  Hello   " (centered within a width of 10 characters)
    20. String Escaping: You can use escape characters to include special characters in strings, such as `\n` for a new line, `\t` for a tab, and `\\` for a backslash.
        Example: `text = "Line 1\nLine 2"`  # This will give you:
        Line 1  Line 2
    21. String Literals: You can define string literals using single quotes, double quotes, or triple quotes.
        Example: `single_quote_string = 'Hello, world!'
        Example: `double_quote_string = "Hello, world!"

    # This can also be used for multi-line strings

"""

# String Concatenation
greeting = "Hello, " + "world!"
print(greeting)  # Output: Hello, world!

# String Single Quotes, Double Quotes and Triple Quotes
single_quote_string = "Hello, world!"
double_quote_string = "Hello, world's!"
triple_quote_string = """This is a multi-line string."""
print(single_quote_string)  # Output: Hello, world!
print(double_quote_string)  # Output: Hello, world!
print(triple_quote_string)  # Output: This is a multi-line string.

# String Immutability
original_string = "Hello"
modified_string = original_string + " World"  # This creates a new string
print(original_string)  # Output: Hello
print(modified_string)  # Output: Hello World
print(type(original_string))  # Output: <class 'str'>
print(type(modified_string))  # Output: <class 'str'>
print(id(original_string))  # Output: Memory address of original_string
print(
    id(modified_string)
)  # Output: Memory address of modified_string (different from original

# String Slicing
text = "Hello, world!"
substring = text[0:5]  # This will give you "Hello"
print(substring)  # Output: Hello

# String Length,find() and count()
text = "Hello, world!"
length = len(text)  # This will give you the length of the string
print(length)  # Output: 13
print(len(text))  # Output: 13
print(text.find("world"))  # Output: 7 (index of the first occurrence of "world")
print(text.count("o"))  # Output: 2 (number of occurrences of "o")

# String Convert into Character List
text = "Hello"
char_list = list(text)  # This will convert the string into a list of characters
print(char_list)  # Output: ['H', 'e', 'l', 'l', 'o']

# String Formatting
name = "Alice"
greeting = f"Hello, {name}!"  # This will give you "Hello, Alice!"
print(greeting)  # Output: Hello, Alice!

# String Comparison
is_equal = "Hello" == "hello"  # This will be False because of case sensitivity
print(is_equal)  # Output: False

# String Membership
is_present = "world" in "Hello, world!"  # This will be True
print(is_present)  # Output: True

# String Splitting and Joining
text = "Hello, world!"
words = text.split(", ")  # This will give you ['Hello', 'world!']
print(words)  # Output: ['Hello', 'world!']
sentence = " ".join(words)  # This will give you "Hello world!"
print(sentence)  # Output: Hello world!

# String Case Conversion
text = "hello world"
upper_text = text.upper()  # This will give you "HELLO WORLD"
print(upper_text)  # Output: HELLO WORLD
lower_text = upper_text.lower()  # This will give you "hello world"
print(lower_text)  # Output: hello world

# String Stripping
text = "  Hello, world!  "
stripped_text = text.strip()  # This will give you "Hello, world!"
print(stripped_text)  # Output: Hello, world!

# String Replacement
text = "Hello, world!"
new_text = text.replace("world", "Python")  # This will give you "Hello, Python!"
print(new_text)  # Output: Hello, Python!

# String Alignment
text = "Hello"
aligned_text = text.center(
    10
)  # This will give you "  Hello   " (centered within a width of 10 characters)
print(aligned_text)  # Output:   Hello

# String Escaping
text = "Line 1\nLine 2"  # This will give you:
print(text)  # Output:
# Line 1
# Line 2

# String using range
text = "Hello, world!"
for i in range(len(text)):
    print(text[i])  # This will print each character in the string on a new line

# String using for loop
text = "Hello, world!"
for char in text:
    print(char)  # This will print each character in the string on a new line

# String using while loop
text = "Hello, world!"
index = 0
while index < len(text):
    print(text[index])  # This will print each character in the string on a new line
    index += 1

# String using list comprehension
text = "Hello, world!"
char_list = [
    char for char in text
]  # This will create a list of characters from the string
print(
    char_list
)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']

# Convert List of Characters into String
char_list = ["H", "e", "l", "l", "o"]
text = "".join(char_list)  # This will convert the list of characters back into a
# string
print(text)  # Output: Hello

# String using map() function
text = "Hello, world!"
char_list = list(
    map(str, text)
)  # This will create a list of characters from the string
print(
    char_list
)  # Output: ['H', 'e', 'l', 'lo', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']

# String using filter() function
text = "Hello, world!"
vowels = "aeiouAEIOU"
vowel_list = list(
    filter(lambda char: char in vowels, text)
)  # This will create a list of vowels from the string
print(vowel_list)  # Output: ['e', 'o', 'o']

# String using reduce() function
from functools import reduce

text = "Hello, world!"
concatenated = reduce(
    lambda x, y: x + y, text
)  # This will concatenate all characters in the string
print(concatenated)  # Output: Hello, world!

# String replace and remove a character and reverse a string
text = "RAMA IS GREAT"
# Replace 'o' with 'x'
replaced_text = text.replace("o", "x")
print(replaced_text)  # Output: Hellx, wxrld!
# Remove 'l' from the string
removed_text = text.replace("l", "")
print(removed_text)  # Output: Heo, word!
# Reverse the string
reversed_text = text[::-1]
print(reversed_text)  # Output: !dlrow ,olleH

# String using endswith() and startswith() method
text = "Hello, world!"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("world!"))  # Output: True

# String using isalpha() and isdigit() method
text = "Hello"
print(text.isalpha())  # Output: True (all characters are alphabetic)
number = "12345"
print(number.isdigit())  # Output: True (all characters are digits)
alphanumeric = "Hello123"
print(alphanumeric.isalnum())  # Output: True (all characters are alphanumeric)
not_alphanumeric = "Hello, world!"
print(
    not_alphanumeric.isalnum()
)  # Output: False (contains non-alphanumeric characters)

# If we want to see entire operation of string
s = "Balaji"
print(dir(s))
