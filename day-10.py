# Program 037: Swap Case of String

text = input("Enter a string: ")

swapped_text = text.swapcase()

print("Original string:", text)
print("After swapping case:", swapped_text)

'''
Sample output:
Enter a string: Hello World
Original string: Hello World
After swapping case: hELLO wORLD

What’s happening?
-The .swapcase() method converts all uppercase letters to lowercase and all lowercase letters to uppercase.
-Non-alphabetic characters (spaces, numbers, symbols) remain unchanged.
-Python provides this built-in method to avoid writing manual loops for case conversion.
'''

# Program 038: Remove Whitespaces

text = input("Enter a string: ")

text_without_spaces = text.replace(" ", "")

print("Original string:", text)
print("String without spaces:", text_without_spaces)

'''
Sample output:
Enter a string: Hello World From Python
Original string: Hello World From Python
String without spaces: HelloWorldFromPython

What’s happening?
-The .replace(" ", "") method replaces every space character with an empty string.
-This removes all spaces from the string but keeps other characters intact.
-It is a simple way to clean up strings when spaces are not needed.
'''

# Program 039: Check if String Contains Only Digits

text = input("Enter a string: ")

if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

'''
Sample output:
Enter a string: 12345
The string contains only digits.

Another example:
Enter a string: 123a45
The string does not contain only digits.

What’s happening?
-The .isdigit() method returns True if all characters in the string are digits and there is at least one character.
-If any character is not a digit (like letters, spaces, or symbols), it returns False.
-This is useful for validating numeric input entered as text.
'''

# Program 040: Convert String to List of CharactersProgram

text = input("Enter a string: ")

char_list = list(text)

print("Original string:", text)
print("List of characters:", char_list)

'''
Sample output:
Enter a string: Python
Original string: Python
List of characters: ['P', 'y', 't', 'h', 'o', 'n']

What’s happening?
-The list() function converts the string into a list where each character becomes a separate element.
-This is helpful when you need to process or modify individual characters.
-Strings are immutable in Python, but lists are mutable, so converting to a list allows changes.
'''