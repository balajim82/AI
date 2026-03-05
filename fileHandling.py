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
    open
    read/write/update
    close

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
