# Program 013: Check Palindrome Number

number = input("Enter a number: ")

reversed_number = number[::-1]

if number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

'''
Output:
Enter a number: 121
The number is a palindrome.

What’s happening?
-A palindrome reads the same from left to right and right to left.
121 → 121
123 → 321

-[::-1] reverses the string. Python supports slicing with a step value, and -1 means moving backward through the string.
'''

# Program 014: Check Armstrong Number

number = int(input("Enter a number: "))

original_number = number
number_of_digits = len(str(number))
digit_power_sum = 0

while number > 0:
    digit = number % 10
    digit_power_sum = digit_power_sum + digit ** number_of_digits
    number = number // 10

if digit_power_sum == original_number:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")

'''
Output:
Enter a number: 153
The number is an Armstrong number.

What’s happening?
For 153:
1³ + 5³ + 3³
= 1 + 125 + 27
= 153

The program:
-Extracts the last digit using % 10.
-Raises the digit to the power of the number of digits.
-Adds it to digit_power_sum.
-Removes the last digit using // 10.
-Compares the final sum with the original number.
'''

# Program 015: Sum of Digits

number = int(input("Enter a positive integer: "))

original_number = number
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum = digit_sum + digit
    number = number // 10

print("The sum of the digits is:", digit_sum)

'''
Output:
Enter a positive integer: 12345
The sum of the digits is: 15

What’s happening?
12345 → 5
1234  → 4
123   → 3
12    → 2
1     → 1

Then:
5 + 4 + 3 + 2 + 1 = 15
-We use the same digit-extraction logic as the reverse-number program.
'''

# Program 016: Find GCD / HCF

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

while second_number != 0:
    remainder = first_number % second_number
    first_number = second_number
    second_number = remainder

print("The GCD/HCF is:", first_number)

'''
Output:
Enter the first number: 48
Enter the second number: 18
The GCD/HCF is: 6

What’s happening?
-The program uses the Euclidean algorithm:
48 ÷ 18 → remainder 12
18 ÷ 12 → remainder 6
12 ÷ 6  → remainder 0

-When the remainder becomes 0, the current value of first_number is the GCD/HCF.
-Python also provides math.gcd() for this task, but we are implementing the logic manually first so you understand how it works.
'''