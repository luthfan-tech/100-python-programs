# Program 049: Intersection of Two Lists

first_data = input("Enter elements for the first list separated by spaces: ")
second_data = input("Enter elements for the second list separated by spaces: ")


first_list = first_data.split()
second_list = second_data.split()


intersection = []


for item in first_list:
    if item in second_list and item not in intersection:
        intersection.append(item)


print("First list:", first_list)
print("Second list:", second_list)
print("Common elements:", intersection)


'''
Sample output:
Enter elements for the first list separated by spaces: apple banana mango orange
Enter elements for the second list separated by spaces: banana grapes mango kiwi
First list: ['apple', 'banana', 'mango', 'orange']
Second list: ['banana', 'grapes', 'mango', 'kiwi']
Common elements: ['banana', 'mango']


What’s happening?
-The program checks every item in the first list.
-If the item also exists in the second list, it is common to both lists.
-The extra condition prevents the same item from being added more than once.
'''

# Program 050: Difference Between Two Lists

first_data = input("Enter elements for the first list separated by spaces: ")
second_data = input("Enter elements for the second list separated by spaces: ")


first_list = first_data.split()
second_list = second_data.split()


difference = []


for item in first_list:
    if item not in second_list and item not in difference:
        difference.append(item)


print("First list:", first_list)
print("Second list:", second_list)
print("Elements only in the first list:", difference)


'''
Sample output:
Enter elements for the first list separated by spaces: apple banana mango orange
Enter elements for the second list separated by spaces: banana grapes mango kiwi
First list: ['apple', 'banana', 'mango', 'orange']
Second list: ['banana', 'grapes', 'mango', 'kiwi']
Elements only in the first list: ['apple', 'orange']


What’s happening?
-The program checks each item in the first list.
-If an item is not present in the second list, it is added to difference.
-The second condition prevents duplicate output items.
'''

# Program 051: Split List into Chunks

data = input("Enter elements separated by spaces: ")
chunk_size = int(input("Enter chunk size: "))


items = data.split()


if chunk_size <= 0:
    print("Chunk size must be greater than zero.")
else:
    chunks = []


    for index in range(0, len(items), chunk_size):
        chunk = items[index:index + chunk_size]
        chunks.append(chunk)


    print("Original list:", items)
    print("Chunks:", chunks)


'''
Sample output:
Enter elements separated by spaces: 1 2 3 4 5 6 7 8 9 10
Enter chunk size: 3
Original list: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
Chunks: [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10']]


What’s happening?
-The range() function moves through the list in steps equal to chunk_size.
-Slicing items[index:index + chunk_size] selects one small section of the list.
-Each small section is added to the chunks list.
-The final chunk can contain fewer elements if the list length is not divisible by the chunk size.
'''

# Program 052: Flatten Nested List

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]


flattened_list = []


for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)


print("Nested list:", nested_list)
print("Flattened list:", flattened_list)


'''
Sample output:
Nested list: [[1, 2, 3], [4, 5], [6, 7, 8]]
Flattened list: [1, 2, 3, 4, 5, 6, 7, 8]


What’s happening?
-A nested list contains lists inside another list.
-The first for loop goes through each inner list.
-The second for loop goes through each item inside that inner list.
-Each item is added to flattened_list, creating one normal list.
'''