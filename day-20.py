# 77. Quick Sort

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    smaller = [num for num in numbers if num < pivot]
    equal = [num for num in numbers if num == pivot]
    greater = [num for num in numbers if num > pivot]

    return quick_sort(smaller) + equal + quick_sort(greater)


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted list:", quick_sort(numbers))

'''
Example input:
10 4 7 2 9 1

Output:
Sorted list: [1, 2, 4, 7, 9, 10]
'''

# 78. Merge Sort

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted list:", merge_sort(numbers))

# 79. Power of a Number Using Recursion

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


base = int(input("Enter base: "))
exponent = int(input("Enter a non-negative exponent: "))

if exponent < 0:
    print("Please enter a non-negative exponent.")
else:
    print(f"{base}^{exponent} = {power(base, exponent)}") 

'''
Example:
Enter base: 2
Enter a non-negative exponent: 5
2^5 = 32
'''
# 80. Tower of Hanoi

'''
Rules
Move only one disk at a time.
A larger disk cannot be placed on a smaller disk.
Use the helper rod when moving disks.

For 𝑛 disks, the minimum number of moves is 2^𝑛−1.
The solution moves 𝑛−1 disks to the helper rod, moves the biggest disk, then moves 𝑛−1 disks onto it. 
'''

def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, helper)

    print(f"Move disk {n} from {source} to {destination}")

    tower_of_hanoi(n - 1, helper, source, destination)


disks = int(input("Enter number of disks: "))

if disks <= 0:
    print("Please enter a positive number of disks.")
else:
    tower_of_hanoi(disks, "A", "B", "C")

'''
For 3 disks, it prints 7 moves. Use a small value like 3 or 4—output grows very quickly.
'''

