# Program 057: Sort Dictionary by Value

student_marks = {
    "Lutfan": 78,
    "Harsha": 92,
    "Karthik": 85,
    "Chiranth": 70
}

sorted_marks = dict(
    sorted(student_marks.items(), key=lambda item: item[1])
)

print("Original dictionary:", student_marks)
print("Dictionary sorted by value:", sorted_marks)

'''
Sample output:
Original dictionary: {'Lutfan': 78, 'Harsha': 92, 'Karthik': 85, 'Chiranth': 70}
Dictionary sorted by value: {'Chiranth': 70, 'Lutfan': 78, 'Karthik': 85, 'Harsha': 92}

What’s happening?
-The .items() method gives both the key and value together as pairs.
-sorted() sorts those pairs.
-key=lambda item: item[1] tells Python to sort using the value, not the key.
-dict() converts the sorted pairs back into a dictionary.
'''

# Program 058: Check Key Existence

student_marks = {
    "Lutfan": 78,
    "Harsha": 92,
    "Karthik": 85,
    "Chiranth": 70
}

key_to_check = input("Enter a student name to check: ")

if key_to_check in student_marks:
    print(f"'{key_to_check}' exists in the dictionary.")
    print("Marks:", student_marks[key_to_check])
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")

'''
Sample output:
Enter a student name to check: Lutfan
'Lutfan' exists in the dictionary.
Marks: 78

Another example:
Enter a student name to check: Arjun
'Arjun' does not exist in the dictionary.

What’s happening?
-The in operator checks whether a key exists in a dictionary.
-If the key exists, student_marks[key_to_check] accesses its value.
-Checking first prevents a KeyError when the key is missing.
'''

# Program 059: Iterate Keys and Values

student_marks = {
    "Lutfan": 78,
    "Harsha": 92,
    "Karthik": 85,
    "Chiranth": 70
}

print("Student marks:")

for student, marks in student_marks.items():
    print(f"{student}: {marks}")

'''
Sample output:
Student marks:
Lutfan: 78
Harsha: 92
Karthik: 85
Chiranth: 70

What’s happening?
-The .items() method returns each dictionary entry as a key-value pair.
-The for loop stores the key in student and the value in marks.
-f-strings make it easy to display both values in a readable format.
'''

# Program 060: Sum All Values in Dictionary

monthly_expenses = {
    "Food": 2500,
    "Travel": 1200,
    "Internet": 600,
    "Learning": 900
}

total_expense = sum(monthly_expenses.values())

print("Monthly expenses:", monthly_expenses)
print("Total expense:", total_expense)

'''
Sample output:
Monthly expenses: {'Food': 2500, 'Travel': 1200, 'Internet': 600, 'Learning': 900}
Total expense: 5200

What’s happening?
-The .values() method gives all values from the dictionary.
-sum() adds those numeric values together.
-This is useful for totals such as expenses, marks, sales, or scores.
'''