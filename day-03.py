# Program 009: Find the Fractional Part of a Number

number = float(input("Enter a decimal number: "))

fractional_part = number - int(number)

print("The fractional part is:", fractional_part)

'''
Output:
Enter a decimal number: 25.75
The fractional part is: 0.75

What’s happening?
-int(number) removes the decimal part.
-number - int(number) leaves only the fractional part.

For 25.75, the calculation is:
25.75 - 25 = 0.75
'''

# Program 010: Check if a Number Is Prime

number = int(input("Enter an integer: "))

if number < 2:
    print("The number is not prime.")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")


'''
Output: 
Enter an integer: 13
The number is prime.

What’s happening?
-A prime number is greater than 1 and can only be divided evenly by 1 and itself.
-The loop tests possible divisors from 2 up to one less than the number. If the remainder is 0, the number has another divisor and is not prime.
'''

# Program 011: Print Fibonacci Series

terms = int(input("Enter the number of terms: "))

first = 0
second = 1

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci series:")
    for _ in range(terms):
        print(first, end=" ")
        first, second = second, first + second


'''
Output:
Enter the number of terms: 8
Fibonacci series:
0 1 1 2 3 5 8 13

What’s happening?
-Each new Fibonacci number is calculated by adding the previous two numbers:
text
0, 1, 1, 2, 3, 5, 8, 13

-The variables keep moving forward:
text
first  → second
second → next
-The for loop repeats the process the requested number of times.
'''

# Program 012: Reverse a Number

number = int(input("Enter a positive integer: "))

original = number
reversed_num = 0

while number > 0:
    reversed_num = (reversed_num * 10) + (number % 10)
    number //= 10

print("Original number:", original)
print("Reversed number:", reversed_num)


'''
Output:
Enter a positive integer: 12345
Original number: 12345
Reversed number: 54321

What’s happening?
For each loop:
-% 10 extracts the last digit.
-That digit is added to the reversed number.
-// 10 removes the last digit from the original number.
-The loop continues until no digits remain.

Example:
12345 → last digit 5
1234  → last digit 4
123   → last digit 3
12    → last digit 2
1     → last digit 1
'''