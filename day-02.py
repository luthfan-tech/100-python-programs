# Program 005: Swap Two Numbers

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

print("Before swapping:")
print("First number:", first_number)
print("Second number:", second_number)

first_number, second_number = second_number, first_number

print("After swapping:")
print("First number:", first_number)
print("Second number:", second_number)

'''
Sample output:
Enter the first number: 10
Enter the second number: 20
Before swapping:
First number: 10
Second number: 20
After swapping:
First number: 20
Second number: 10

What’s happening?
-The value of first_number is stored temporarily. Then the second value is moved into the first variable, and the saved value is moved into the second variable.
'''

# Program 006: Find the Largest of Three Numbers

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

if first_number >= second_number and first_number >= third_number:
    largest = first_number
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
else:
    largest = third_number

print("The largest number is:", largest)

'''
Sample output:
Enter the first number: 25
Enter the second number: 14
Enter the third number: 19
The largest number is: 25.0

-What’s happening?
The if and elif conditions compare each number with the other two. The number that is greater than or equal to both others is stored in largest. Python uses conditional statements to choose which block of code should run.
'''

# Program 007: Check Even or Odd

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

'''
Sample output:
Enter an integer: 12
The number is even.

Another example:
Enter an integer:  seven

That would cause an error because the program expects an integer. Use:
7
Output:
The number is odd.

What’s happening?
The % operator gives the remainder after division. If a number divided by 2 has a remainder of 0, it is even; otherwise, it is odd.
'''

# Program 008: Check Positive or Negative

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

'''
Sample output:
Enter a number: -8
The number is negative.

For zero:
Enter a number: 0
The number is zero.

What’s happening?
-Python checks three possibilities:
-Greater than 0 means positive.
-Less than 0 means negative.
-Exactly 0 means zero.
-The comparison operators and if/elif/else structure allow the program to make decisions.
'''