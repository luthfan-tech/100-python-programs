# 85. Copy File Contents

# This copies everything from sample.txt into copy_sample.txt.
import shutil

source_file = "sample.txt"
destination_file = "copy_sample.txt"

try:
    shutil.copyfile(source_file, destination_file)
    print(f"Contents copied from {source_file} to {destination_file}.")

except FileNotFoundError:
    print(f"{source_file} was not found.")
# shutil.copyfile() copies file contents from the source file to the destination file. 


# 86. Exception Handling Example

# This handles invalid input and division by zero safely.
try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    result = number1 / number2

except ValueError:
    print("Invalid input. Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")

'''
Try these inputs:
10 and 2     → Result: 5.0
10 and 0     → You cannot divide by zero.
abc and 2    → Invalid input.
'''

# 87. Custom Exception Class

# This program creates a custom exception for an invalid age.
class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

    print("You are eligible.")

except ValueError:
    print("Please enter a valid whole number.")

except InvalidAgeError as error:
    print("Custom Exception:", error)
# A custom exception is simply a class that inherits from Exception, then you trigger it with raise when your program’s own rule is broken.


# 88. Check if File Exists

from pathlib import Path

file_name = input("Enter file name: ")

file_path = Path(file_name)

if file_path.exists():
    print(f"'{file_name}' exists.")
else:
    print(f"'{file_name}' does not exist.")

'''
Example input:
sample.txt

Example output:
'sample.txt' exists.

pathlib.Path provides an object-oriented way to work with file paths, and it is generally cleaner than manually managing path strings. 
'''

'''
Run order:
1.Make sure sample.txt exists.
2.Run Program 85 to create copy_sample.txt.
3.Run Program 88 using both sample.txt and a random filename.
4.Run Program 86 with valid, zero, and invalid inputs.
5.Run Program 87 with ages below and above 18.
'''
