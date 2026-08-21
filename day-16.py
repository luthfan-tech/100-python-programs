# Program 061: Invert Dictionary (Swap Keys & Values)

student_marks = {
    "Lutfan": 78,
    "Harsha": 92,
    "Karthik": 85,
    "Chiranth": 70
}

inverted_dictionary = {}

for key, value in student_marks.items():
    inverted_dictionary[value] = key

print("Original dictionary:", student_marks)
print("Inverted dictionary:", inverted_dictionary)

'''
Sample output:
Original dictionary: {'Lutfan': 78, 'Harsha': 92, 'Karthik': 85, 'Chiranth': 70}
Inverted dictionary: {78: 'Lutfan', 92: 'Harsha', 85: 'Karthik', 70: 'Chiranth'}

What’s happening?
-The .items() method provides each key-value pair from the dictionary.
-The new dictionary uses the old value as its key and the old key as its value.
-Important: dictionary values should be unique before inverting. If two students have the same marks, one name would replace the other in the inverted dictionary.
'''

# Program 062: Find Max and Min Key by Value

student_marks = {
    "Lutfan": 78,
    "Rahul": 92,
    "Karthik": 85,
    "Priya": 70
}

highest_student = max(student_marks, key=student_marks.get)
lowest_student = min(student_marks, key=student_marks.get)

print("Student marks:", student_marks)
print("Student with highest marks:", highest_student)
print("Highest marks:", student_marks[highest_student])
print("Student with lowest marks:", lowest_student)
print("Lowest marks:", student_marks[lowest_student])

'''
Sample output:
Student marks: {'Lutfan': 78, 'Rahul': 92, 'Karthik': 85, 'Priya': 70}
Student with highest marks: Rahul
Highest marks: 92
Student with lowest marks: Priya
Lowest marks: 70

What’s happening?
-By default, max() and min() would compare the dictionary keys alphabetically.
-key=student_marks.get tells Python to compare keys using their associated values instead.
-max() returns the key with the largest value, while min() returns the key with the smallest value.
'''

# Program 063: Remove Key from Dictionary

student_marks = {
    "Lutfan": 78,
    "Rahul": 92,
    "Karthik": 85,
    "Priya": 70
}

key_to_remove = input("Enter the student name to remove: ")

if key_to_remove in student_marks:
    removed_marks = student_marks.pop(key_to_remove)

    print(f"Removed '{key_to_remove}' with marks: {removed_marks}")
    print("Updated dictionary:", student_marks)
else:
    print(f"'{key_to_remove}' does not exist in the dictionary.")

'''
Sample output:
Enter the student name to remove: Priya
Removed 'Priya' with marks: 70
Updated dictionary: {'Lutfan': 78, 'Rahul': 92, 'Karthik': 85}

Another example:
Enter the student name to remove: Arjun
'Arjun' does not exist in the dictionary.

What’s happening?
-The in operator checks whether the key exists before trying to remove it.
-The .pop() method removes the key-value pair and returns its value.
-Checking first prevents a KeyError if the entered name does not exist.
'''

# Program 064: Combine Two Lists into Dictionary

keys_data = input("Enter dictionary keys separated by spaces: ")
values_data = input("Enter dictionary values separated by spaces: ")


keys = keys_data.split()
values = values_data.split()


if len(keys) != len(values):
    print("The number of keys and values must be the same.")
else:
    combined_dictionary = dict(zip(keys, values))

    print("Keys:", keys)
    print("Values:", values)
    print("Combined dictionary:", combined_dictionary)


'''
Sample output:
Enter dictionary keys separated by spaces: name language database tool
Enter dictionary values separated by spaces: Lutfan Python SQL GitHub
Keys: ['name', 'language', 'database', 'tool']
Values: ['Lutfan', 'Python', 'SQL', 'GitHub']
Combined dictionary: {'name': 'Lutfan', 'language': 'Python', 'database': 'SQL', 'tool': 'GitHub'}


Another example:
Enter dictionary keys separated by spaces: name age city
Enter dictionary values separated by spaces: Lutfan 18 Mumbai       
The number of keys and values must be the same.


What’s happening?
-The split() method turns both input strings into lists.
-zip(keys, values) pairs each key with the value in the same position.
-dict() converts those pairs into a dictionary.
-The length check prevents missing keys or values.
'''
