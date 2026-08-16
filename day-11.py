# Program 041: Find Max and Min in List

numbers = input("Enter numbers separated by spaces: ")

num_list = [float(x) for x in numbers.split()]

if len(num_list) == 0:
    print("The list is empty.")
else:
    maximum = max(num_list)
    minimum = min(num_list)
    
    print("List of numbers:", num_list)
    print("Maximum value:", maximum)
    print("Minimum value:", minimum)

'''
Sample output:
Enter numbers separated by spaces: 5 12 3 8 20 1
List of numbers: [5.0, 12.0, 3.0, 8.0, 20.0, 1.0]
Maximum value: 20.0
Minimum value: 1.0

What’s happening?
-The input string is split into parts and converted to a list of floats.
-The built-in max() and min() functions find the largest and smallest values.
-This avoids writing manual loops and uses Python’s optimized functions.
'''

# Program 042: Sum & Average of List Elements

numbers = input("Enter numbers separated by spaces: ")

num_list = [float(x) for x in numbers.split()]

if len(num_list) == 0:
    print("The list is empty.")
else:
    total_sum = sum(num_list)
    average = total_sum / len(num_list)
    
    print("List of numbers:", num_list)
    print("Sum of elements:", total_sum)
    print("Average of elements:", average)

'''
Sample output:
Enter numbers separated by spaces: 10 20 30 40
List of numbers: [10.0, 20.0, 30.0, 40.0]
Sum of elements: 100.0
Average of elements: 25.0

What’s happening?
-The sum() function adds all elements in the list.
-The average is calculated by dividing the sum by the number of elements.
-Using built-in functions makes the code shorter and less error-prone.
'''

# Program 043: Remove Duplicates from List

data = input("Enter elements separated by spaces: ")

original_list = data.split()
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original list:", original_list)
print("List without duplicates:", unique_list)

'''
Sample output:
Enter elements separated by spaces: 1 2 3 2 4 1 5
Original list: ['1', '2', '3', '2', '4', '1', '5']
List without duplicates: ['1', '2', '3', '4', '5']

What’s happening?
-A new list (unique_list) is created to store only unique elements.
-The for loop checks each item; if it’s not already in unique_list, it is added.
-This preserves the original order while removing duplicates.
'''

# Program 044: Count Occurrences of Element

data = input("Enter elements separated by spaces: ")

elements = data.split()

target = input("Enter the element to count: ")

count = elements.count(target)

print("Original list:", elements)
print(f"Occurrences of '{target}':", count)

'''
Sample output:
Enter elements separated by spaces: apple banana apple orange apple
Enter the element to count: apple
Original list: ['apple', 'banana', 'apple', 'orange', 'apple']
Occurrences of 'apple': 3

What’s happening?
-The .count() method returns how many times a value appears in the list.
-This is useful for frequency analysis and simple statistics.
-It avoids writing a manual loop for counting.
'''