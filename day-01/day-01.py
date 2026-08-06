# Program 001: Hello World

print("Hello, World!")

#Output: Hello, World!

'''
What's happening?
Python executes the print() function and displays the text written inside the parentheses.

Explanation:
-print() is a built-in Python function.
-"Hello, World!" is a string.
-Text must be surrounded by quotation marks.
-Python displays the string exactly as written.
'''

# Program 002: Add Two Numbers

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

total = first_number + second_number

print("The sum is:", total)

'''
Output:
Enter the first number: 10
Enter the second number: 20
The sum is: 30.0

What’s happening?
-Python asks the user for the first number.
-The entered value is converted from text into a decimal number.
-The same process happens for the second number.
-Python adds both values.
-The result is stored in total.
-The answer is displayed.

Explanation:
-input() receives data from the user.
-float() converts the input into a number.
-first_number and second_number are variables.
-+ performs addition.
-total stores the result.
'''

# Program 003: Multiply Two Numbers

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

product = first_number * second_number

print("The product is:", product)

'''
Output:
Enter the first number: 6
Enter the second number: 7
The product is: 42.0

What’s happening?
-The program asks for two numbers.
-float() converts both inputs into numbers.
-The * operator multiplies the numbers.
-The result is stored in product.
-print() displays the result.

Explanation:
-* is Python’s multiplication operator.
-product is the variable containing the multiplication result.
-The program uses the same input and conversion process as Program 002.
-The name product clearly describes the result of multiplication.
'''

# Program 004: Average of Three Numbers

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

average = (first_number + second_number + third_number) / 3

print("The average is:", average)



'''
Output:
Enter the first number: 10
Enter the second number: 20
Enter the third number: 30
The average is: 20.0

What’s happening?
-The program collects three numbers.
-Each input is converted into a decimal number.
-The three numbers are added together.
-Their total is divided by 3.
-The final result is stored in average.
-Python displays the average.

Explanation
The formula for the average is:
average = total of values / number of values
'''