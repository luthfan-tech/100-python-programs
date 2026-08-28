# 89. Read CSV File

'''
First create a file named students.csv in the same folder:
name,age,course
Jordan,20,Python
Khabeeb,21,Data Science
Cristiano,19,Web Development
'''

# Now use this Python program:
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("students.csv was not found.")
'''
Expected output:
['name', 'age', 'course']
['Asif', '20', 'Python']
['Ayaan', '21', 'Data Science']
['Sara', '19', 'Web Development']
'''

# Better version: read rows by column name
import csv

try:
    with open("students.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}, Course: {row['course']}")

except FileNotFoundError:
    print("students.csv was not found.")

# 90. Class & Object Creation
# A class is a blueprint; an object is one real instance created from it.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Lutfan Mohammed Asif", 20, "Python")
student2 = Student("Ayaan", 21, "Web Development")

student1.display_details()
print()
student2.display_details()

# 91. Single Inheritance
# Single inheritance means one child class inherits from one parent class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


class Developer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def show_skill(self):
        print(f"I am learning {self.language}.")


developer1 = Developer("Lutfan Mohammed Asif", 20, "Python")

developer1.introduce()
developer1.show_skill()

# 92. Encapsulation: Private Variables

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Lutfan Mohammed Asif", 5000)

account.deposit(1500)
account.withdraw(2000)

print("Current balance: ₹", account.get_balance())

'''
Do not try to access account.__balance directly. In Python, a double-underscore field triggers name mangling rather than true strict privacy; it is mainly designed to avoid accidental name clashes, especially with subclasses. 
'''


'''
# Run order
89 → Create students.csv and run CSV reader
90 → Run class/object program
91 → Run single-inheritance program
92 → Run encapsulation program
'''