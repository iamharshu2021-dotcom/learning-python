# Day 5 - Types of Errors in Python
# Simple and basic examples with explanations in comments.
#
# Every example below is wrapped in try/except so the whole file runs
# without crashing. In real code, an unhandled error stops the program.


# ==================== 1. SYNTAX ERROR ====================
# Happens when the code breaks Python's grammar rules.
# Python finds it BEFORE running the program.
# Common causes: missing colon, missing bracket, missing quote.

print("----- 1. SyntaxError -----")

# We use exec() here only to show the error safely.
try:
    exec("print('Hello'")   # closing bracket is missing
except SyntaxError as e:
    print("SyntaxError:", e)

# Other examples (these would stop the program if written directly):
# if 5 > 3          <- colon missing
# print("Hello)     <- closing quote missing


# ==================== 2. INDENTATION ERROR ====================
# Python uses spaces at the start of a line to define code blocks.
# Wrong or missing spaces cause an IndentationError.

print("\n----- 2. IndentationError -----")

try:
    exec("if True:\nprint('Hello')")   # the print line is not indented
except IndentationError as e:
    print("IndentationError:", e)


# ==================== 3. NAME ERROR ====================
# Happens when we use a variable or function that is not defined.
# Common causes: spelling mistake, using a variable before creating it.

print("\n----- 3. NameError -----")

try:
    print(score)   # 'score' was never created
except NameError as e:
    print("NameError:", e)


# ==================== 4. TYPE ERROR ====================
# Happens when an operation is used on the wrong data type.

print("\n----- 4. TypeError -----")

try:
    result = "Age: " + 20   # cannot add a string and an integer
except TypeError as e:
    print("TypeError:", e)

# Fix: convert the number to a string first
print("Fixed:", "Age: " + str(20))


# ==================== 5. VALUE ERROR ====================
# Happens when the type is correct but the value is not suitable.

print("\n----- 5. ValueError -----")

try:
    number = int("hello")   # "hello" cannot become an integer
except ValueError as e:
    print("ValueError:", e)


# ==================== 6. INDEX ERROR ====================
# Happens when we use an index that does not exist in a list or tuple.

print("\n----- 6. IndexError -----")

fruits = ["apple", "banana", "mango"]   # valid indexes are 0, 1, 2

try:
    print(fruits[5])
except IndexError as e:
    print("IndexError:", e)


# ==================== 7. KEY ERROR ====================
# Happens when we use a key that does not exist in a dictionary.

print("\n----- 7. KeyError -----")

student = {"name": "Harsh", "age": 20}

try:
    print(student["city"])
except KeyError as e:
    print("KeyError: key not found ->", e)

# Fix: get() returns None (or a default value) instead of an error
print("Using get():", student.get("city", "Not available"))


# ==================== 8. ZERO DIVISION ERROR ====================
# Happens when we divide a number by zero.

print("\n----- 8. ZeroDivisionError -----")

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)


# ==================== 9. ATTRIBUTE ERROR ====================
# Happens when we use a method or attribute that the object does not have.

print("\n----- 9. AttributeError -----")

numbers = [1, 2, 3]

try:
    numbers.add(4)   # lists have append(), not add()
except AttributeError as e:
    print("AttributeError:", e)


# ==================== 10. IMPORT ERROR ====================
# Happens when a module cannot be imported.
# ModuleNotFoundError is a type of ImportError.

print("\n----- 10. ModuleNotFoundError -----")

try:
    import my_fake_module
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)


# ==================== 11. FILE NOT FOUND ERROR ====================
# Happens when we try to open a file that does not exist.

print("\n----- 11. FileNotFoundError -----")

try:
    file = open("no_such_file.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)


# ==================== 12. LOGICAL ERROR ====================
# The program runs without any error message, but the answer is WRONG.
# Python cannot detect it, we must find it by checking the output.

print("\n----- 12. Logical Error -----")

a = 10
b = 20
average = a + b / 2   # wrong: division happens first
print("Wrong average:", average)

average = (a + b) / 2   # correct: use brackets
print("Correct average:", average)


# ==================== HANDLING ERRORS ====================
# try      -> code that may cause an error
# except   -> runs if an error happens
# else     -> runs if NO error happens
# finally  -> always runs, error or not

print("\n----- Handling errors: try, except, else, finally -----")

try:
    number = int("25")
    print("Number is:", number)
except ValueError:
    print("Please enter a valid number")
else:
    print("No error happened")
finally:
    print("This line always runs")

# Handling more than one error type
try:
    x = 10
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value")

# Catching any error with the base class Exception
try:
    print(undefined_variable)
except Exception as e:
    print("Some error happened:", e)


# ==================== RAISING OUR OWN ERROR ====================
# We can create an error ourselves using the raise keyword.

print("\n----- raise -----")

age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("ValueError:", e)


# ==================== SUMMARY ====================
# SyntaxError         wrong Python grammar (missing colon, bracket, quote)
# IndentationError    wrong spaces at the start of a line
# NameError           variable or function is not defined
# TypeError           wrong data type used in an operation
# ValueError          right type but wrong value
# IndexError          list/tuple index is out of range
# KeyError            dictionary key not found
# ZeroDivisionError   dividing by zero
# AttributeError      method or attribute does not exist
# ImportError         module cannot be imported
# FileNotFoundError   file does not exist
# Logical error       no error message, but the output is wrong
