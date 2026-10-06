# Python for Data Analytics: Day 1

Fundamentals: Print, Variables, Data Types, Input and Type Conversion

Author: Harsh Mishra  
Course: B.Tech AI/ML, Kanpur Institute of Technology  
Language: Python 3

## Topics Covered

| No. | Topic | Key idea |
|---|---|---|
| 1 | print() | Display output using sep, end and f-strings |
| 2 | Variables | Store values with = and multiple assignment |
| 3 | Data Types | int, float, str, bool, list and type() |
| 4 | input() | Read user input, always returned as a string |
| 5 | Type Conversion | Convert values using int(), float(), str(), list() |

## 1. The print() Function

print() displays output on the screen. By default it separates multiple values with a space and ends with a new line. The sep argument changes the separator and the end argument changes what is printed at the end. An f-string (a string starting with f) lets you place variables directly inside text using curly braces.

Example:

```python
print("Hello, World!")
print("My name is Harsh Mishra")

# sep and end
print("Python", "is", "fun", sep="-")
print("Line 1", end=" | ")
print("Line 2")

# f-string
name = "Harsh"
print(f"My name is {name}")
```

Output:

```text
Hello, World!
My name is Harsh Mishra
Python-is-fun
Line 1 | Line 2
My name is Harsh
```

Key points:

- Text must be inside quotes.
- sep controls what goes between values, end controls what comes after the last value.
- f-strings are the cleanest way to mix text and variables.

## 2. Variables

A variable is a name that refers to a stored value. In Python you create a variable by assigning a value with the = sign. There is no need to declare its type in advance. Python also supports assigning several variables in one line.

Example:

```python
name = "Harsh"
age = 20
college = "KIT"
print(name, age, college)

# Multiple assignment
a, b, c = 1, 2, 3

# Same value for multiple variables
x = y = z = 100
print(a, b, c, x, y, z)
```

Output:

```text
Harsh 20 KIT
1 2 3 100 100 100
```

Key points:

- Variable names are case sensitive: age and Age are different.
- Names cannot start with a digit or contain spaces. Use snake_case, for example total_marks.
- A variable can be reassigned to a new value at any time.

## 3. Data Types

Every value in Python has a type. The basic types used most often are int (whole numbers), float (decimal numbers), str (text), bool (True or False) and list (an ordered collection of values). The built-in type() function tells you the type of any value.

| Type | Meaning | Example |
|---|---|---|
| `int` | Whole number | 85 |
| `float` | Decimal number | 78.5 |
| `str` | Text | "AI/ML" |
| `bool` | True or False | True |
| `list` | Ordered collection | ["NumPy", "Pandas"] |

Example:

```python
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
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'list'>
```

Key points:

- Python decides the type automatically from the value.
- Booleans must be written as True or False with a capital first letter.

## 4. Taking Input

input() pauses the program and waits for the user to type something. The value it returns is always a string, even if the user types digits. To do arithmetic you must first convert it, for example with int() or float().

Example:

```python
name = input("What is your name? ")
print("My name is", name)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
print("Total is", num1 + num2)
```

Output:

```text
What is your name? Harsh
My name is Harsh
Enter number 1: 10
Enter number 2: 20
Total is 30
```

Key points:

- input() always returns a string.
- Wrap input() with int() or float() when you need a number.
- The text inside input() is the prompt shown to the user.

## 5. Type Conversion

Type conversion (also called type casting) changes a value from one type to another. The main functions are int(), float(), str() and list(). Converting a float to an int removes the decimal part. It does not round the number.

Example:

```python
# String to int
num = int("25")
print(num + 5)

# int to float, float to int
print(float(10))
print(int(9.8))

# Number to string, string to list
print("Age: " + str(20))
print(list("abc"))
```

Output:

```text
30
10.0
9
Age: 20
['a', 'b', 'c']
```

Key points:

- int(9.8) gives 9, not 10. The decimal part is cut off.
- int("abc") raises a ValueError because the text is not a number.
- You cannot add a string and a number directly. Convert one of them first.

## Common Mistake: Forgetting to Convert Input

Because input() returns a string, adding two inputs joins them instead of adding them.

```python
a = input("Enter 5: ")      # user types 5, but a is the string "5"
print(a + a)                # 55  (strings are joined)
print(int(a) + int(a))      # 10  (numbers are added)
```

## Practice Exercises

1. Ask the user for their name and age, then print: Hello <name>, you will be <age + 1> next year.
2. Take two numbers from the user and print their sum, difference, product and division.
3. Store your marks in 5 subjects in variables and print the total and the average.
4. Take a temperature in Celsius from the user and convert it to Fahrenheit (F = C * 9/5 + 32).
5. Print the type of five different values of your own choice.

## Quick Recap

- print() shows output. Use sep, end and f-strings to control it.
- Variables store values and do not need a declared type.
- Core data types: int, float, str, bool, list. Check them with type().
- input() always returns a string.
- Use int(), float(), str() and list() to convert between types.

Next: Day 2 - Operators and Conditional Statements (if, elif, else)
