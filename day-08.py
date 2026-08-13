# Program 029: Remove Vowels from String

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
result = ""

for character in text:
    if character not in vowels:
        result = result + character

print("Original string:", text)
print("String without vowels:", result)

'''
Sample output:
Enter a string: May the force be with you
Original string: May the force be with you
String without vowels: My th frc b wth y

What’s happening?
-We define vowels as both lowercase and uppercase vowel letters.
-We loop through each character in text.
-If a character is not a vowel, we add it to result.
-Spaces and punctuation are kept as they are.
'''

# Program 030: Count Character Frequency

text = input("Enter a string: ")

frequency = {}

for character in text:
    if character != " ":  # ignore spaces; remove this check to count spaces too
        if character in frequency:
            frequency[character] = frequency[character] + 1
        else:
            frequency[character] = 1

print("Character frequencies:")

for character, count in frequency.items():
    print(f"'{character}' → {count}")

'''
Sample output:
Enter a string: hello world
Character frequencies:
'h' → 1
'e' → 1
'l' → 3
'o' → 2
'w' → 1
'r' → 1
'd' → 1

What’s happening?
-We create an empty dictionary called frequency.
For each non-space character:
If it’s already in the dictionary, we increase its count.
-Otherwise, we add it with a count of 1.
-Then we print each character and how many times it appears.
-This is the classic “frequency counting” pattern: building a dictionary (hash map) of counts and then iterating over it.
'''

# Program 031: Remove Duplicate Characters

text = input("Enter a string: ")

seen_characters = set()
result = ""

for character in text:
    if character not in seen_characters:
        seen_characters.add(character)
        result = result + character

print("Original string:", text)
print("String without duplicate characters:", result)

'''
Sample output:
Enter a string: programming
Original string: programming
String without duplicate characters: progamin

What’s happening?
-seen_characters is a set that stores characters we have already encountered.
For each character:
-If it has not been seen before, we add it to the set and to result.
-If it has already been seen, we skip it.
-The first occurrence of every character is kept, later duplicates are removed.
'''

# Program 032: Check Anagram

first_text = input("Enter the first string: ")
second_text = input("Enter the second string: ")

normalized_first = first_text.replace(" ", "").lower()
normalized_second = second_text.replace(" ", "").lower()

if len(normalized_first) != len(normalized_second):
    print("The strings are not anagrams.")
else:
    sorted_first = sorted(normalized_first)
    sorted_second = sorted(normalized_second)

    if sorted_first == sorted_second:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

'''
Sample output:
Enter the first string: listen
Enter the second string: silent
The strings are anagrams.

Another example:
Enter the first string: conversation
Enter the second string: voices rant on
The strings are anagrams.

What’s happening?
-We normalize the strings by:
removing spaces,
converting to lowercase.
-If the lengths are different, they can’t be anagrams.
-We sort the characters in both strings with sorted() and compare:
If the sorted lists match, the strings contain the same characters in the same counts → they are anagrams.
'''
