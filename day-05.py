
# PROGRAM 017 — FIND LCM
first_number = int(input("Enter the first positive number: "))
second_number = int(input("Enter the second positive number: "))

larger_number = max(first_number, second_number)
lcm = larger_number

while lcm % first_number != 0 or lcm % second_number != 0:
    lcm = lcm + larger_number

print("The LCM is:", lcm)

'''
Output:
Enter the first positive number: 12
Enter the second positive number: 18
The LCM is: 36
'''

# PROGRAM 018 — COUNT DIGITS IN AN INTEGER
number = int(input("Enter an integer: "))

number_without_sign = abs(number)

if number_without_sign == 0:
    digit_count = 1
else:
    digit_count = 0

    while number_without_sign > 0:
        number_without_sign = number_without_sign // 10
        digit_count = digit_count + 1

print("Number of digits:", digit_count)

'''
Output:
Enter an integer: 12345
Number of digits: 5
'''

# PROGRAM 019 — CHECK LEAP YEAR
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year.")
elif year % 100 == 0:
    print("It is not a leap year.")
elif year % 4 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")

'''
Output:
Enter a year: 2020
It is a leap year.
'''

# PROGRAM 020 — MULTIPLICATION TABLE
number = int(input("Enter a number: "))

print("Multiplication table of", number)

for multiplier in range(1, 11):
    result = number * multiplier
    print(number, "x", multiplier, "=", result)

'''
Output:
Enter a number: 5
Multiplication table of 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''
