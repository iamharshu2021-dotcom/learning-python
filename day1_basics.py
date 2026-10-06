"""
Python for Data Analytics - Day 1
Author: Harsh Mishra
Topics: print, variables, data types, input, type conversion
"""

# ---------- 1. print ----------
print("Hello, World!")
print("My name is Harsh Mishra")
print("Currently I am learning Python for data analytics")

print("Python", "is", "fun", sep="-")
print("Line 1", end=" | ")
print("Line 2")

# ---------- 2. variables ----------
name = "Harsh"
age = 20
college = "KIT"
print(name, age, college)
print(f"My name is {name}")

a, b, c = 1, 2, 3          # multiple assignment
x = y = z = 100            # same value for many variables

# ---------- 3. data types ----------
marks = 85                                  # int
percentage = 78.5                           # float
subject = "AI/ML"                           # str
passed = True                               # bool
topics = ["NumPy", "Pandas", "Sklearn"]     # list

print(type(marks))
print(type(percentage))
print(type(subject))
print(type(passed))
print(type(topics))

# ---------- 4. input ----------
user_name = input("What is your name? ")
print("My name is", user_name)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print("Total is", num1 + num2)

# ---------- 5. type conversion ----------
num = int("25")
print(num + 5)

print(float(10))
print(int(9.8))             # 9, the decimal part is removed (no rounding)

print("Age: " + str(20))
print(list("abc"))
