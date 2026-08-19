# Program 053: Check if List is Sorted

data = input("Enter numbers separated by spaces: ")


numbers = [float(item) for item in data.split()]


is_sorted = True


for index in range(len(numbers) - 1):
    if numbers[index] > numbers[index + 1]:
        is_sorted = False
        break


print("List:", numbers)


if is_sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")


'''
Sample output:
Enter numbers separated by spaces: 2 5 8 10 14
List: [2.0, 5.0, 8.0, 10.0, 14.0]
The list is sorted in ascending order.


Another example:
Enter numbers separated by spaces: 2 8 5 10
List: [2.0, 8.0, 5.0, 10.0]
The list is not sorted in ascending order.


What’s happening?
-The loop compares each number with the number immediately after it.
-If a number is greater than the next number, the list is not in ascending order.
-The break statement stops checking as soon as Python finds an unsorted pair.
'''

# Program 054: Find Common Elements Across 3 Lists

first_data = input("Enter elements for the first list separated by spaces: ")
second_data = input("Enter elements for the second list separated by spaces: ")
third_data = input("Enter elements for the third list separated by spaces: ")


first_list = first_data.split()
second_list = second_data.split()
third_list = third_data.split()


common_elements = []


for item in first_list:
    if item in second_list and item in third_list and item not in common_elements:
        common_elements.append(item)


print("First list:", first_list)
print("Second list:", second_list)
print("Third list:", third_list)
print("Common elements in all three lists:", common_elements)


'''
Sample output:
Enter elements for the first list separated by spaces: apple banana mango orange
Enter elements for the second list separated by spaces: banana mango grapes apple
Enter elements for the third list separated by spaces: kiwi mango apple banana
First list: ['apple', 'banana', 'mango', 'orange']
Second list: ['banana', 'mango', 'grapes', 'apple']
Third list: ['kiwi', 'mango', 'apple', 'banana']
Common elements in all three lists: ['apple', 'banana', 'mango']


What’s happening?
-The program checks each item in the first list.
-An item is common only if it also appears in both the second and third lists.
-The final condition avoids adding duplicate items to common_elements.
'''

# Program 055: Cumulative Sum of List

data = input("Enter numbers separated by spaces: ")


numbers = [float(item) for item in data.split()]


cumulative_sum = []
running_total = 0


for number in numbers:
    running_total += number
    cumulative_sum.append(running_total)


print("Original list:", numbers)
print("Cumulative sum list:", cumulative_sum)


'''
Sample output:
Enter numbers separated by spaces: 2 4 6 8
Original list: [2.0, 4.0, 6.0, 8.0]
Cumulative sum list: [2.0, 6.0, 12.0, 20.0]


What’s happening?
-running_total starts at 0.
-The loop adds each number to the running total.
-After every addition, the current total is stored in cumulative_sum.
-For example: 2 → 2 + 4 = 6 → 6 + 6 = 12 → 12 + 8 = 20.
'''

# Program 056: Merge Two Dictionaries    

first_dictionary = {
    "name": "Lutfan",
    "language": "Python",
    "level": "Beginner"
}


second_dictionary = {
    "database": "SQL",
    "tool": "GitHub",
    "level": "Learning"
}


merged_dictionary = first_dictionary.copy()
merged_dictionary.update(second_dictionary)


print("First dictionary:", first_dictionary)
print("Second dictionary:", second_dictionary)
print("Merged dictionary:", merged_dictionary)


'''
Sample output:
First dictionary: {'name': 'Lutfan', 'language': 'Python', 'level': 'Beginner'}
Second dictionary: {'database': 'SQL', 'tool': 'GitHub', 'level': 'Learning'}
Merged dictionary: {'name': 'Lutfan', 'language': 'Python', 'level': 'Learning', 'database': 'SQL', 'tool': 'GitHub'}


What’s happening?
-The copy() method creates a copy of the first dictionary.
-The update() method adds all key-value pairs from the second dictionary.
-If both dictionaries have the same key, the value from the second dictionary replaces the first value.
-In this example, the value of level changes from Beginner to Learning.
'''