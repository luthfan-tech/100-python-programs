# Program 045: Sort List (Ascending/Descending)

data = input("Enter numbers separated by spaces: ")


numbers = [float(x) for x in data.split()]


if len(numbers) == 0:
    print("The list is empty.")
else:
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    
    print("Original list:", numbers)
    print("Sorted (ascending):", ascending)
    print("Sorted (descending):", descending)


'''
Sample output:
Enter numbers separated by spaces: 5 12 3 8 20 1
Original list: [5.0, 12.0, 3.0, 8.0, 20.0, 1.0]
Sorted (ascending): [1.0, 3.0, 5.0, 8.0, 12.0, 20.0]
Sorted (descending): [20.0, 12.0, 8.0, 5.0, 3.0, 1.0]


What’s happening?
-The sorted() function returns a new sorted list from the original.
-By default, it sorts in ascending order.
-Passing reverse=True sorts in descending order.
-This avoids writing manual sorting logic and uses Python’s optimized implementation.
'''

# Program 046: Find Second Largest Number

data = input("Enter numbers separated by spaces: ")


numbers = [float(x) for x in data.split()]


if len(numbers) < 2:
    print("Not enough elements to find the second largest.")
else:
    unique_numbers = []
    for n in numbers:
        if n not in unique_numbers:
            unique_numbers.append(n)
    
    if len(unique_numbers) < 2:
        print("No distinct second largest number (all values may be the same).")
    else:
        unique_numbers.sort(reverse=True)
        second_largest = unique_numbers[1]
        
        print("Original list:", numbers)
        print("Unique numbers:", unique_numbers)
        print("Second largest number:", second_largest)


'''
Sample output:
Enter numbers separated by spaces: 5 12 3 12 8 20 1
Original list: [5.0, 12.0, 3.0, 12.0, 8.0, 20.0, 1.0]
Unique numbers: [20.0, 12.0, 8.0, 5.0, 3.0, 1.0]
Second largest number: 12.0


What’s happening?
-Duplicates are removed to get distinct numbers.
-The unique list is sorted in descending order.
-The element at index 1 is the second largest.
-This handles cases where the largest value appears multiple times.
'''

# Program 047: Merge Two Lists

list1_data = input("Enter elements for the first list (separated by spaces): ")
list2_data = input("Enter elements for the second list (separated by spaces): ")


list1 = list1_data.split()
list2 = list2_data.split()


merged_list = list1 + list2


print("First list:", list1)
print("Second list:", list2)
print("Merged list:", merged_list)


'''
Sample output:
Enter elements for the first list (separated by spaces): 1 2 3
Enter elements for the second list (separated by spaces): 4 5 6
First list: ['1', '2', '3']
Second list: ['4', '5', '6']
Merged list: ['1', '2', '3', '4', '5', '6']


What’s happening?
-The + operator concatenates two lists into a new list.
-Elements from the first list come first, followed by elements from the second list.
-This is a simple and efficient way to merge lists in Python.
'''

# Program 048: Rotate List by K Positions

data = input("Enter elements separated by spaces: ")
k = int(input("Enter the number of positions to rotate: "))


elements = data.split()


if len(elements) == 0:
    print("The list is empty.")
else:
    k = k % len(elements)  # handle k larger than list length
    
    rotated_list = elements[-k:] + elements[:-k]
    
    print("Original list:", elements)
    print("Rotated list:", rotated_list)


'''
Sample output:
Enter elements separated by spaces: 1 2 3 4 5
Enter the number of positions to rotate: 2
Original list: ['1', '2', '3', '4', '5']
Rotated list: ['4', '5', '1', '2', '3']


Another example (left rotation effect with positive k):
Enter elements separated by spaces: a b c d e
Enter the number of positions to rotate: 3
Original list: ['a', 'b', 'c', 'd', 'e']
Rotated list: ['c', 'd', 'e', 'a', 'b']


What’s happening?
-The list is split into two parts using slicing:
 - elements[-k:] takes the last k elements.
 - elements[:-k] takes the remaining front part.
-These two parts are concatenated to form the rotated list.
-Using k % len(elements) ensures the rotation works even if k is larger than the list length.
'''