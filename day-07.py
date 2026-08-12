# Program 025: Square Root of a Number

import math

number = float(input("Enter a non-negative number: "))

if number < 0:
    print("Square root of a negative number is not a real number.")
else:
    square_root = math.sqrt(number)
    print("The square root is:", square_root)

'''
Sample output:
Enter a non-negative number: 16
The square root is: 4.0

What’s happening?
-math.sqrt(number) calculates the square root of the given value.
-We check for negative input so the program stays beginner-friendly and avoids confusing complex numbers.
'''

# Program 026: Reverse a String

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Original string:", text)
print("Reversed string:", reversed_text)

'''
Sample output:
Enter a string: python
Original string: python
Reversed string: nohtyp

What’s happening?
-text[::-1] uses string slicing with a step of -1 to traverse the string from end to start, effectively reversing it.
'''

# Program 027: Check String Palindrome

text = input("Enter a string: ")

normalized_text = text.replace(" ", "").lower()
reversed_text = normalized_text[::-1]

if normalized_text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''
Sample output:
Enter a string: Level
The string is a palindrome.

Another example:
Enter a string: never odd or even
The string is a palindrome.

What’s happening?
-replace(" ", "") removes spaces.
-lower() converts all letters to lowercase.
-[::-1] reverses the cleaned string.
-If the cleaned original equals the reversed one, it is a palindrome.
'''

# Program 028: Count Vowels and Consonants

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for character in text:
    if character.isalpha():
        if character in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

'''
Sample output:
Enter a string: May the force be with you
Number of vowels: 8
Number of consonants: 15

What’s happening?
-isalpha() checks whether the character is a letter.
-If the letter is in the string vowels, we increase vowel_count.
-Otherwise, it is treated as a consonant and consonant_count is increased.
-This pattern (loop + membership check) is a standard way to count vowels and consonants in a string.

'''