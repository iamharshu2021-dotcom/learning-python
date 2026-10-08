# Day 3 - Python Loops Practice (while loops & for loops)

# Practice 0: print the same thing multiple times
print("meow")
print("meow")
print("meow")

# Practice 1: while loop (prints 4 times, i = 0,1,2,3)
i = 0
while i <= 3:
    print("hello world")
    i = i + 1

# Practice 2: for loop with a list
for i in [0, 1, 2]:
    print("hello world")

# Practice 3: string multiplication (not a good practice for loops, but it works)
print("hello world\n" * 3)

# Practice 4: while loop - print 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Practice 5: while loop - print 10 to 1 (reverse)
i = 10
while i >= 1:
    print(i)
    i -= 1

# Practice 6: while loop - sum of 1 to 10
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)

# Practice 7: while loop - multiplication table
num = int(input("Enter number: "))
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# Practice 8: while loop - digit counter
num = int(input("Enter number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits =", count)

# Practice 9: for loop with range - print 1 to 10
for i in range(1, 11):
    print(i)

# Practice 10: for loop with range step - even numbers 2 to 20
for i in range(2, 21, 2):
    print(i)

# Practice 11: for loop with a list
fruits = ["Apple", "Mango", "Banana", "Orange"]
for fruit in fruits:
    print(fruit)

# Practice 12: multiplication table using for loop
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
