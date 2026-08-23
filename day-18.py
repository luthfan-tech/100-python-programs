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

Note: this basic recursive version becomes slow for large numbers because it repeats calculations. It’s perfect for learning recursion, thoug
'''