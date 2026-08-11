# PROGRAM 021 — CELSIUS TO FAHRENHEIT

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

'''
OUTPUT:
Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.0

WHAT IS HAPPENING:
-The program receives a temperature in Celsius and applies the conversion -formula:
Fahrenheit = (Celsius × 9 / 5) + 32
For 25°C:
(25 × 9 / 5) + 32 = 77°F
-The input is converted to float so the program can accept decimal temperatures such as 36.5.
'''

# PROGRAM 022 — SIMPLE INTEREST

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest

print("Simple interest:", simple_interest)
print("Total amount:", amount)

'''
OUTPUT:
Enter the principal amount: 10000
Enter the annual rate of interest: 5
Enter the time in years: 2
Simple interest: 1000.0
Total amount: 11000.0

WHAT IS HAPPENING:
-The program uses the simple-interest formula:
-Simple Interest = (Principal × Rate × Time) / 100
-Then it calculates the final amount:
-Total Amount = Principal + Simple Interest

For this example:
Simple Interest = (10000 × 5 × 2) / 100 = 1000
Total Amount = 10000 + 1000 = 11000
'''

# PROGRAM 023 — COMPOUND INTEREST

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest: "))
time = float(input("Enter the time in years: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound interest:", round(compound_interest, 2))
print("Total amount:", round(amount, 2))

'''
OUTPUT:
Enter the principal amount: 10000
Enter the annual rate of interest: 5
Enter the time in years: 2
Compound interest: 1025.0
Total amount: 11025.0

WHAT IS HAPPENING:
-The program uses the compound-interest formula:
-Amount = Principal × (1 + Rate / 100) ^ Time
-Then it finds the interest:
Compound Interest = Amount - Principal

For this example:
Amount = 10000 × (1 + 5 / 100)²
Amount = 11025
Compound Interest = 11025 - 10000 = 1025

The ** operator means exponentiation, or raising a number to a power.
round(value, 2) displays the result rounded to two decimal places.
'''

# PROGRAM 024 — AREA OF A CIRCLE

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2

print("The area of the circle is:", round(area, 2))

'''
OUTPUT:
Enter the radius of the circle: 7
The area of the circle is: 153.94

WHAT IS HAPPENING:
-The program uses the formula:
-Area = π × radius²
-math.pi provides the value of π, approximately 3.14159.

For a radius of 7:
Area = π × 7²
Area = π × 49
Area ≈ 153.94

-radius ** 2 means radius multiplied by itself.


CONCEPTS PRACTISED
===================

- float() for decimal input
- Mathematical formulas
- Variables
- Arithmetic operators
- Exponentiation with **
- Importing the math module
- math.pi
- round() for cleaner output
- Printing multiple results
'''