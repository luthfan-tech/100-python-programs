# 69. Recursive Factorial

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

'''
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120.
'''

# 70. Recursive Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


terms = int(input("Enter number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")

'''
Output for 7 terms:
0 1 1 2 3 5 8

Note: this basic recursive version becomes slow for large numbers because it repeats calculations. It’s perfect for learning recursion, though.
'''

# 71. Recursive Sum of Natural Numbers

def sum_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_natural_numbers(n - 1)


num = int(input("Enter a positive number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    print(f"Sum of natural numbers from 1 to {num} is {sum_natural_numbers(num)}")

'''
Example: for 5, result is 1 + 2 + 3 + 4 + 5 = 15.
'''

# 72. Linear Search

def linear_search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to search: "))

result = linear_search(numbers, target)

if result == -1:
    print(f"{target} was not found in the list.")
else:
    print(f"{target} was found at index {result}.") 

'''
Example input:
Enter numbers separated by spaces: 10 25 30 45 60
Enter the number to search: 45

Output:
45 was found at index 3.

Linear search checks each item from the beginning until it finds the target or reaches the end.
'''