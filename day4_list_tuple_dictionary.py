# Day 4 - Python Data Structures: List, Tuple, Dictionary, Set
# Simple and basic examples with explanations in comments.


# ==================== LIST ====================
# A list stores many items in one variable.
# It is ordered, changeable (mutable) and allows duplicates.
# It is written with square brackets [].

print("----- LIST -----")

fruits = ["apple", "banana", "mango"]
print(fruits)

# Access items by index (index starts from 0)
print(fruits[0])    # first item
print(fruits[-1])   # last item

# Slicing: list[start:stop] (stop is not included)
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]

# Change an item
fruits[1] = "grapes"
print(fruits)

# Add items
fruits.append("orange")        # add at the end
fruits.insert(1, "kiwi")       # add at a given index
print(fruits)

# Remove items
fruits.remove("kiwi")          # remove by value
fruits.pop()                   # remove the last item
print(fruits)

# Useful functions
nums = [5, 2, 8, 1]
print(len(nums))     # number of items
print(max(nums))     # biggest item
print(min(nums))     # smallest item
print(sum(nums))     # total of all items
nums.sort()          # sort in ascending order
print(nums)

# Loop through a list
for fruit in fruits:
    print(fruit)


# ==================== TUPLE ====================
# A tuple is like a list, but it cannot be changed (immutable).
# It is written with round brackets ().

print("\n----- TUPLE -----")

colors = ("red", "green", "blue")
print(colors)

# Access items by index, same as a list
print(colors[0])
print(colors[-1])

# Tuple cannot be changed, so this would give an error:
# colors[0] = "yellow"

# Tuple methods
numbers = (1, 2, 2, 3)
print(numbers.count(2))   # how many times 2 appears
print(numbers.index(3))   # position of 3

# Unpacking: store each item in a separate variable
name, age = ("Harsh", 20)
print(name)
print(age)

# Loop through a tuple
for color in colors:
    print(color)


# ==================== DICTIONARY ====================
# A dictionary stores data as key : value pairs.
# It is written with curly brackets {}.
# Keys must be unique.

print("\n----- DICTIONARY -----")

student = {
    "name": "Harsh",
    "age": 20,
    "branch": "AI/ML"
}
print(student)

# Access a value using its key
print(student["name"])
print(student.get("age"))   # get() does not give an error if key is missing

# Add a new key and value
student["city"] = "Kanpur"

# Change an existing value
student["age"] = 21
print(student)

# Remove an item
student.pop("city")
print(student)

# Get all keys, values and items
print(student.keys())
print(student.values())
print(student.items())

# Loop through a dictionary
for key, value in student.items():
    print(key, ":", value)

# Check if a key exists
print("name" in student)


# ==================== SET ====================
# A set stores unique items only (no duplicates).
# It is unordered, so there is no index.

print("\n----- SET -----")

my_set = {1, 2, 3, 3, 2}
print(my_set)   # duplicates are removed

my_set.add(4)
my_set.remove(1)
print(my_set)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union: all items from both
print(a & b)   # intersection: common items
print(a - b)   # difference: in a but not in b


# ==================== SUMMARY ====================
# List       []        ordered, changeable, allows duplicates
# Tuple      ()        ordered, NOT changeable, allows duplicates
# Dictionary {k: v}    key-value pairs, keys are unique
# Set        {}        unordered, no duplicates
