"""
1. Error handling module for the application.
2. Provides functions to log errors and display user-friendly messages.
3. Uses the built-in logging module to log errors to a file.
4. Contains a custom exception class for application-specific errors.
5. Ensures that all exceptions are caught and handled gracefully to prevent application crashes.
6. Provides a function to send error reports to the development team for further analysis.
7. Includes a function to display error messages to users in a user-friendly manner, without exposing technical details.
8. Implements a retry mechanism for certain types of errors, such as network errors, to improve user experience.
9. Contains a function to validate user input and raise appropriate exceptions if the input is invalid.
10. Provides a function to handle uncaught exceptions globally, ensuring that all errors are logged and handled appropriately.
11. Uses a configuration file to specify error handling settings, such as log file location and error reporting email address.
12. Provides a function to categorize errors based on severity levels (e.g., critical, warning, info) for better error management.
13. Implements a mechanism to suppress certain non-critical errors from being logged or displayed to users, based on user preferences or application settings.
14.  Below Sample structure of the module:
     try:
         # Code that may raise an exception
     except SpecificException as e:
         # Handle specific exception
     except Exception as e:
         # Handle general exceptions
     finally:
         # Code that will run regardless of whether an exception occurred or not
15. What are some common practices for error handling in Python?
        - Use try-except blocks to catch and handle exceptions.
        - Use specific exception types to handle different kinds of errors appropriately.
        - Log errors to a file for later analysis.
        - Display user-friendly error messages to users.
        - Use finally blocks to ensure that certain code runs regardless of whether an exception occurred or not.
        - Avoid using bare except clauses, as they can catch unexpected exceptions and make debugging more difficult.
        - Use custom exception classes for application-specific errors to provide more context and clarity.
 16. What are checked and unchecked exceptions in Python, and how do they differ from each other?
        - In Python, there is no distinction between checked and unchecked exceptions as in some other programming languages like Java.
          All exceptions in Python are unchecked, meaning that they do not need to be declared or caught explicitly.
          Developers can choose to handle exceptions using try-except blocks, but it is not mandatory.
          This allows for more flexibility in error handling, but it also means that developers need to be diligent in catching and handling exceptions appropriately to prevent application crashes.

 17. What are the benefits of using an error handling module in an application?
        - Centralized error management: All error handling logic is contained in one module, making it easier to maintain and update.
        - Improved user experience: By displaying user-friendly error messages, users are less likely to be frustrated by technical details.
        - Better debugging: Logging errors to a file allows developers to analyze and fix issues more efficiently
        - Enhanced reliability: Proper error handling can prevent application crashes and ensure that the application continues to function even when errors occur.
        - Increased security: By not exposing technical details in error messages, the application is less vulnerable
            to attacks that exploit error information.

 18. Implement a simple error handling module in Python that includes a custom exception class, a function to log errors, and a function to display user-friendly error messages.


"""

#  Sample code for the error handling module;Give input  by user to test the error handling mechanism;
input_value = 10  # input("Enter a number to divide: ")
myBaseValue = 100
try:
    result = myBaseValue / int(input_value)  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero. Pleas20e provide a non-zero value.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Error handling complete.")


# How to create a custom exception class in Python:
class CustomError(Exception):
    """Custom exception for application-specific errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# Example usage of the custom exception:
def validate_input(value):
    if value < 0:
        raise CustomError("Input value cannot be negative.")
    return value


try:
    user_input = -1  # input("Enter a non-negative number: ")
    validate_input(user_input)
except CustomError as e:
    print(f"Custom error occurred: {e.message}")
finally:
    print("Input validation complete.")

# Function to log errors to a file
import logging


def log_error(error_message):
    logging.basicConfig(filename="d:\\error_log.txt", level=logging.ERROR)
    logging.error(error_message)


try:
    # Simulate an error
    raise ValueError("This is a test error.")
except Exception as e:
    log_error(str(e))
    print("An error has been logged.")
finally:
    print("Error logging complete.")


# Function to display user-friendly error messages
def display_error_message(error_message):
    print(f"An error occurred: {error_message}. Please try again.")


try:
    # Simulate an error
    raise ValueError("This is a test error.")
except Exception as e:
    display_error_message(str(e))
finally:
    print("Error message displayed.")


# Function to handle uncaught exceptions globally
import sys
import traceback


def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    log_error(
        "Uncaught exception: "
        + "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    )
    print("An unexpected error occurred. Please contact support.")


sys.excepthook = global_exception_handler
# Simulate an uncaught exception
raise ValueError("This is an uncaught test error.")


# Function to categorize errors based on severity levels
def categorize_error(error_message, severity):
    if severity == "critical":
        log_error(f"CRITICAL: {error_message}")
    elif severity == "warning":
        log_error(f"WARNING: {error_message}")
    elif severity == "info":
        log_error(f"INFO: {error_message}")
    else:
        log_error(f"UNKNOWN SEVERITY: {error_message}")


try:
    # Simulate an error with severity
    raise ValueError("This is a critical test error.")
except Exception as e:
    categorize_error(str(e), "critical")
    print("A critical error has been logged.")
finally:
    print("Error categorization complete.")
