# 73. Binary Search

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return mid
        elif target > numbers[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter number to search: "))

result = binary_search(numbers, target)

if result == -1:
    print(f"{target} was not found.")
else:
    print(f"{target} was found at index {result}.")

'''
Example input:
Enter sorted numbers: 10 20 30 40 50 60
Enter number to search: 40

Output:
40 was found at index 3.
'''

# 74. Bubble Sort

def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted list:", bubble_sort(numbers))

# 75. Selection Sort

def selection_sort(numbers):
    n = len(numbers)

    for i in range(n):
        smallest_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[smallest_index]:
                smallest_index = j

        numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

    return numbers


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted list:", selection_sort(numbers))

# 76. Insertion Sort

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted list:", insertion_sort(numbers))
