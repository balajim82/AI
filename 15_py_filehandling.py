"""
1. File handling functions for the project.
2. This module provides functions to read and write files, as well as to manage file paths.
3. It includes functions to read text files, write text files, and check if a file exists.
4. The functions in this module are designed to be simple and easy to use, making it easier to handle files in the project.
5. The module also includes error handling to ensure that file operations are performed safely and to provide informative error messages when something goes wrong.
6. Overall, this module is an essential part of the project, as it allows for efficient and effective file management, which is crucial for the success of any project that involves data storage and retrieval.
7. The functions in this module can be used in various parts of the project, such as for reading configuration files, writing logs, and managing data files.
8. By using the functions in this module, developers can save time and effort when working with files, as they can rely on the provided functions to handle common file operations without having to write custom code for each operation.
9. In summary, the file handling functions in this module are an important tool for any developer working on the project, as they provide a convenient and efficient way to manage files and ensure that file operations are performed safely and effectively.
10. Major functions in this module include:
  - read_file(file_path): Reads the contents of a file and returns it as a string
  - write_file(file_path, content): Writes the given content to a file at the specified path
  - file_exists(file_path): Checks if a file exists at the specified path and returns a boolean value
  - delete_file(file_path): Deletes the file at the specified path if it exists
  - update_file(file_path, content): Updates the contents of a file by appending new content to it, rather than overwriting the existing content.
  - get_file_size(file_path): Returns the size of a file in bytes, which can be useful for managing storage and ensuring that files do not exceed certain size limits.
  - read and write JSON files: Functions to read and write JSON files, which are commonly used for storing structured data in a human-readable format.
  - write and read CSV files: Functions to handle CSV files, which are widely used for storing tabular data and can be easily imported into spreadsheet applications.
11. Major Modes of Use:
    - Reading a file: Use the read_file function to read the contents of a file and store it in a variable for further processing.
    - Writing to a file: Use the write_file function to write content to a file, either by creating a new file or overwriting an existing one.
    - Checking for file existence: Use the file_exists function to check if a file exists before attempting to read from or write to it, preventing errors.
    - Deleting a file: Use the delete_file function to remove a file from the system when it is no longer needed, ensuring that storage space is managed effectively.
    - Updating a file: Use the update_file function to append new content to an existing file without overwriting the current contents, allowing for incremental updates.
    - Managing file sizes: Use the get_file_size function to check the size of a file before performing operations that may require a certain amount of storage space, helping to prevent issues related to insufficient storage.
    - Handling JSON files: Use the provided functions to read and write JSON files for structured data
    - Handling CSV files: Use the provided functions to read and write CSV files for tabular data, making it easier to work with data in spreadsheet applications.
12. Any File below things should remember:
     Modes of operation
        Read - 'r'
        Write - 'w'
        Append - 'a'
        Read & Write - 'r+'
        Write & Read - 'w+'
        append & Read - 'a+'
Detail Description of Modes and it's Importence
Read Mode
===============
# Read mode - 'r'
# When we open a file in read mode
# 1. If file exist then it will open the file in read mode and places the cursor at the begining of the file
# 2. If file does not Exist, FileNotFoundError
# 3. You are allowed only to read from file but not allowed to write into the file.
# If file does not exist
# f = open('f1.txt', 'r')  # FileNotFoundError: [Errno 2] No such file or directory: 'f1.txt'
# f.close()

# File Exist
# f = open('my_mod.py', 'r')
# print(f.tell())
# print(f.read())
# print(f.tell())
# # f.write('Hello')   # UnsupportedOperation: not writable
# f.close()

Write mode
===========
# Write mode - 'w'
# When we open a file in Write mode
# 1. If file exist then it will open the file in write mode and places the cursor at the begining of the file after deleting the conetnt of the file
# 2. If file does not Exist then it creates a file with the given name
# 3. You are allowed only to write into file but not allowed to read from the file.


# If file does not exist
# f = open('f1.txt', 'w')
# f.close()

f = open('my_mod.py', 'w')
print(f.tell())
# print(f.read())  # UnsupportedOperation: not readable
f.write('Hello')
print(f.tell())
f.close()

append Mode
=================
# Append mode - 'a'
# When we open a file in append mode
# 1. If file exist then it will open the file in append mode and places the cursor at the end of the file
# 2. If file does not Exist then it creates a file with the given name
# 3. You are allowed only to write into file but not allowed to read from the file.

# f = open('my_mod.py', 'a')
# print(f.tell())
# f.write('\n\nHello')
# print(f.tell())
# print(f.read()) # UnsupportedOperation: not readable
# f.close()

# f = open('f2.py', 'a')
# f.close()

read+ Mode
=========
# Read and write mode - 'r+'
# When we open a file in read and write mode
# 1. If file exist then it will open the file in read mode and places the cursor at the begining of the file
# 2. If file does not Exist, FileNotFoundError
# 3. You are allowed to read and write both

# If file does not exist
# f = open('f1.py', 'r')  # FileNotFoundError: [Errno 2] No such file or directory: 'f1.txt'
# f.close()

# File Exist
f = open('/content/test.txt', 'r+')
print(f.tell())
f.write('\n\nHello')
print(f.read())
print(f.tell())
print(f.tell())
f.close()

write+ Mode
=============
# Write and read mode - 'w+'
# When we open a file in Write mode
# 1. If file exist then it will open the file in write mode and places the cursor at the begining of the file after deleting the conetnt of the file
# 2. If file does not Exist then it creates a file with the given name
# 3. You are allowed to read and write both


# If file does not exist
# f = open('f1.txt', 'w')
# f.close()

f = open('my_mod.py', 'w+')
print(f.tell())
print(f.read())
f.write('Hello')
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read())
f.close()

a+ Mode
============
# Append and read mode - 'a+'
# When we open a file in append mode
# 1. If file exist then it will open the file in append mode and places the cursor at the end of the file
# 2. If file does not Exist then it creates a file with the given name
# 3. You are allowed to read and write both

# f = open('my_mod.py', 'a+')
# print(f.tell())
# f.write('\n\nHello')
# print(f.tell())
# print(f.read())
# f.seek(0)
# print(f.read())
# f.close()

# f = open('f2.py', 'a')
# f.close()

13. # binary files  -- This one more concept in python.
  But it's not so efficient and we can use advance Libraries panda,numpy or pdfruf
    # Read - 'rb'
    # write - 'wb'
    # append - 'ab'
    # read & write - 'rb+'
    # write and read - 'wb+'
    # append and read - 'ab+'

Note:- This file handling concept generally use for basic operations in local file
 to read and write operation. For majority applications uses advance Libs.

14. Benefits of Using with Statement for File Operations - compare to Manually open and close files.
    # BAD: Manual file handling
    f = open('data.txt', 'r')
    content = f.read()
    f.close()  # Easy to forget!

    # What if an error occurs before close()?
    f = open('data.txt', 'r')
    content = f.read()
    result = process_data(content)  # If this fails...
    f.close()  # ...this never executes! File stays open!

    Problems:
      File stays open if you forget f.close()
      File stays open if exception occurs
      Resource leak (too many open files crashes program)
      File locked on Windows (can't delete/modify)

    With with - Automatic Cleanup:
    # ✅ GOOD: Automatic file handling
    with open('data.txt', 'r') as f:
        content = f.read()
        result = process_data(content)
    # File automatically closed here, even if error occurs!

    print(f.closed)  # True - file is closed

    Benefits:
        File always closes, even with exceptions
        No memory leaks
        Clean, readable code
        No need to remember close()


"""


# Simple and read file function and close file after reading
def read_file(file_path):
    """Reads the contents of a file and returns it as a string."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            file.close()
            return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except IOError as e:
        print(f"IOError while reading the file '{file_path}': {e}")
        return None


# call the function to read a file
file_content = read_file("example.txt")
print(file_content)


# Simple and write file function and close file after writing
def write_file(file_path, content):
    """Writes the given content to a file at the specified path."""
    try:
        with open(file_path, "a") as file:
            file.write(content)
            file.close()
    except IOError as e:
        print(f"IOError while writing to the file '{file_path}': {e}")


# call the function to write to a file
write_file("example.txt", "Python invented in 1991 by Guido van Rossum.")
file_content = read_file("example.txt")
print(file_content)

# Simple and check file exists function
import os


def file_exists(file_path):
    """Checks if a file exists at the specified path and returns a boolean value."""
    return os.path.isfile(file_path)


# call the function to check if a file exists
if file_exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# Simple and update file function and close file after updating
def update_file(file_path, content):
    """Updates the contents of a file by appending new content to it, rather than overwriting the existing content."""
    try:
        with open(file_path, "a") as file:
            file.write(content)
            file.close()
    except IOError as e:
        print(f"IOError while updating the file '{file_path}': {e}")


# call the function to update a file
update_file("example.txt", "Python is a high-level, interpreted programming language.")


# Simple and delete file function
def delete_file(file_path):
    """Deletes the file at the specified path if it exists."""
    try:
        if file_exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        else:
            print(f"File '{file_path}' does not exist.")
    except IOError as e:
        print(f"IOError while deleting the file '{file_path}': {e}")


# call the function to delete a file
# delete_file("example.txt")
# call the function to check if a file exists
if file_exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# Simple and get file size function and close file after getting size
def get_file_size(file_path):
    """Returns the size of a file in bytes."""
    try:
        if file_exists(file_path):
            size = os.path.getsize(file_path)
            return size
        else:
            print(f"File '{file_path}' does not exist.")
            return None
    except IOError as e:
        print(f"IOError while getting the size of the file '{file_path}': {e}")
        return None


# call the function to get the size of a file and print into mb
file_size = get_file_size("example.txt")
print(f"Size of 'example.txt': {file_size / (1024 * 1024):.2f} MB")

# Simple and read JSON file function and close file after reading
import json


def read_json_file(file_path):
    """Reads the contents of a JSON file and returns it as a Python object."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            file.close()
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError while reading the file '{file_path}': {e}")
        return None
    except IOError as e:
        print(f"IOError while reading the file '{file_path}': {e}")
        return None


# call the function to read a JSON file
json_data = read_json_file("example.json")
print(json_data)


# Simple in exisitng file  read same structure and append new data into it and close file after writing
# Exameple of existing JSON file content:[
#     {
#         "employee": {
#             "salary": 50000,
#             "name": "balaji",
#             "age": 30,
#             "department": "IT",
#             "skills": ["python", "java", "sql"]
#         }
#     }
# ]
# from the above sample, read it and append skills set with ""c++"" and write back to the same file
def update_json_file(file_path, new_data):
    """Updates the contents of a JSON file by appending new data to it."""
    try:
        if file_exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                file.close()
            data.append(new_data)
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
                file.close()
        else:
            print(f"File '{file_path}' does not exist.")
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError while updating the file '{file_path}': {e}")
    except IOError as e:
        print(f"IOError while updating the file '{file_path}': {e}")


# call the function to update a JSON file
new_employee = {
    "employee": {
        "salary": 60000,
        "name": "suresh",
        "age": 28,
        "department": "HR",
        "skills": ["communication", "recruitment", "training"],
    }
}
update_json_file("example.json", new_employee)


# Simple and write JSON file function and close file after writing
def write_json_file(file_path, data):
    """Writes the given data to a JSON file at the specified path."""
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
            file.close()
    except IOError as e:
        print(f"IOError while writing to the file '{file_path}': {e}")


# call the function to write to a JSON file
employee_data = [
    {
        "employee": {
            "salary": 50000,
            "name": "balaji",
            "age": 30,
            "department": "IT",
            "skills": ["python", "java", "sql"],
        }
    },
    {
        "employee": {
            "salary": 60000,
            "name": "suresh",
            "age": 28,
            "department": "HR",
            "skills": ["communication", "recruitment", "training"],
        }
    },
]
write_json_file("example.json", employee_data)


# ============ WITHOUT WITH - UNSAFE ============
f = open("config.json", "r")
try:
    data = json.load(f)
    # process(data)
finally:
    f.close()  # Must use try-finally to ensure cleanup

# ============ WITH WITH - SAFE & CLEAN ============
with open("config.json", "r") as f:
    data = json.load(f)
    # process(data)
# Automatically closed, even if json.load() or process() fails


# ============ READING AND WRITING SIMULTANEOUSLY ============

# ❌ BAD: Manual handling of multiple files
input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

try:
    for line in input_file:
        output_file.write(line.upper())
finally:
    input_file.close()
    output_file.close()

# ✅ GOOD: Clean handling of multiple files
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line.upper())
# Both files automatically closed

# Cleaner, More Readable Code
# ============ READABILITY COMPARISON ============


# ❌ VERBOSE: 8 lines for simple operation
def read_config_verbose():
    f = None
    try:
        f = open("config.json", "r")
        config = json.load(f)
        return config
    finally:
        if f:
            f.close()


# ✅ CONCISE: 3 lines for same operation
def read_config_clean():
    with open("config.json", "r") as f:
        return json.load(f)


# Works with Any Context Manager
# -- This sample with stament usgae in DB conncetionpoint of view
# ============ DATABASE CONNECTIONS ============
import sqlite3

# Auto-commit/rollback
with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?)", ("Alice", 30))
# Auto-commits on success, auto-rolls back on error

# ============ TEMPORARY FILES ============
import tempfile

# ✅ Auto-delete temp file
with tempfile.NamedTemporaryFile(mode="w", delete=True) as tmp:
    tmp.write("temporary data")
    tmp.flush()
    # Use temp file
# File automatically deleted
