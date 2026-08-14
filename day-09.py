# Program 033: Check Positive or Negative

text = input("Enter a sentence: ")

capitalized_text = text.title()

print("Original sentence:", text)
print("Capitalized sentence:", capitalized_text)

'''
Sample output:
Enter a sentence: hello world from python
Original sentence: hello world from python
Capitalized sentence: Hello World From Python

What’s happening?
-The .title() method converts the first character of each word to uppercase and the rest to lowercase.
-Python treats spaces as word boundaries, so it automatically detects where each word starts.
'''

# Program 034: Check Positive or Negative

text = input("Enter a sentence: ")

words = text.split()
word_count = len(words)

print("Original sentence:", text)
print("Number of words:", word_count)

'''
Sample output:
Enter a sentence: I am learning Python programming
Original sentence: I am learning Python programming
Number of words: 5

What’s happening?
-The .split() method splits the string at every space by default, creating a list of words.
-len() counts how many items are in that list, which gives the total number of words.
'''

# Program 035: Check Positive or Negative

text = input("Enter a sentence: ")

words = text.split()

if len(words) == 0:
    print("No words found.")
else:
    longest_word = words[0]
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    print("Original sentence:", text)
    print("Longest word:", longest_word)

'''
Sample output:
Enter a sentence: Python is a powerful programming language
Original sentence: Python is a powerful programming language
Longest word: programming

What’s happening?
-The sentence is split into a list of words.
-The first word is assumed to be the longest initially.
-The for loop checks each word; if a longer word is found, it replaces the current longest_word.
-At the end, the longest word found is printed.
'''

# Program 036: Check Positive or Negative

main_text = input("Enter a sentence or text: ")
substring = input("Enter the substring to search: ")

if substring in main_text:
    print("Substring found.")
else:
    print("Substring not found.")

'''
Sample output:
Enter a sentence or text: I am learning Python programming
Enter the substring to search: Python
Substring found.

Another example:
Enter a sentence or text: I am learning Python programming
Enter the substring to search: Java
Substring not found.

What’s happening?
-The in operator checks whether the substring exists anywhere inside the main_text.
-If it finds a match, the condition is True; otherwise, it is False.
-This is a simple and efficient way to search for text inside text in Python.
'''