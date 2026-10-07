# Day 2 - Conditional Statements in Python
# Topics: if / elif / else, comparison operators, logical operators, % operator, match-case

# ---------------------------------------------------------
# Example 1: Password check (while loop + if/else + break)
# ---------------------------------------------------------
password = input("What is your password: ")
while True:
    if password == "harsh":
        print("Welcome sir")
        break
    else:
        print("Sorry sir")
        break


# ---------------------------------------------------------
# Example 2: Compare two numbers (if / elif)
# ---------------------------------------------------------
x = int(input("What is x: "))
y = int(input("What is y: "))

if x > y:
    print("x is greater than y")
elif y > x:
    print("y is greater than x")
elif y == x:
    print("Both are equal")


# ---------------------------------------------------------
# Example 3: Grade calculator (and operator)
# ---------------------------------------------------------
score = int(input("Score: "))

if score <= 100 and score >= 90:
    print("Grade A")
elif score < 90 and score >= 80:
    print("Grade B")
elif score < 80 and score >= 70:
    print("Grade C")
elif score < 70 and score >= 60:
    print("Grade D")
else:
    print("Grade F")


# ---------------------------------------------------------
# Example 4: Even or Odd (modulus operator %)
# ---------------------------------------------------------
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# ---------------------------------------------------------
# Example 5: Hogwarts house (if / elif / else with strings)
# ---------------------------------------------------------
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


# ---------------------------------------------------------
# Example 6: Hogwarts house using match-case
# ---------------------------------------------------------
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
