# 93. Polymorphism Example

class Dog:
    def sound(self):
        print("Dog says: Woof Woof")


class Cat:
    def sound(self):
        print("Cat says: Meow Meow")


class Cow:
    def sound(self):
        print("Cow says: Moo Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()

'''
Output:
Dog says: Woof Woof
Cat says: Meow Meow
Cow says: Moo Moo
'''

# 94. Simple Decorator

def greeting_decorator(function):
    def wrapper():
        print("----- Start -----")
        function()
        print("----- End -----")

    return wrapper


@greeting_decorator
def greet():
    print("Hello, Lutfan!")


greet()

'''
Output:
----- Start -----
Hello, Lutfan!
----- End -----
'''

# 95. Generator Example (yield).

def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


for number in even_numbers(10):
    print(number)

'''
Output:
2
4
6
8
10
'''

# 96. Get Current Date and Time

from datetime import datetime

current_date_time = datetime.now()

print("Current date and time:", current_date_time)
print("Date:", current_date_time.strftime("%d-%m-%Y"))
print("Time:", current_date_time.strftime("%I:%M:%S %p"))
# Your date/time output changes based on when you run it.
