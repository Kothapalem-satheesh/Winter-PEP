# DAY-3 DataTypes and understanding slicing advanced slicing techniques


## Table of Contents
1. [Introduction](#introduction)
2. [Basic Data Types](#basic-data-types)
3. [Collection Data Types](#collection-data-types)
4. [Understanding Slicing](#understanding-slicing)
5. [Advanced Slicing Techniques](#advanced-slicing-techniques)
6. [Practical Applications](#practical-applications)
7. [Performance Tips](#performance-tips)
8. [Best Practices](#best-practices)

---

## Introduction

### What are Data Types? - The Toolbox Story

Imagine you're opening a bakery. You need different containers to store different items:
- A **cardboard box** for storing whole cakes (integers)
- A **plastic container** with precise measurements for flour (floats)
- A **label** on each product describing it (strings)
- A **yes/no form** for inventory checklist (booleans)
- **Shelves** that hold multiple items together (lists and tuples)
- A **recipe book** with ingredient names and quantities (dictionaries)
- A **collection basket** for unique items only (sets)

Data types are the classification of data that tells the computer how to interpret and work with that data. Think of data types as different containers in a toolbox - each container holds a specific type of tool.

In Python, data types define:
- **What kind of value** can be stored
- **How much memory** is needed
- **What operations** can be performed on that value
- **How the value behaves** in your program

### What is Slicing? - The Pizza Party Story

Imagine you've ordered a large pizza for a party. The pizza arrives as one whole circular pie. But you need to:
- Give the first 3 slices to your best friend
- Keep every other slice for yourself
- Give the last 2 slices to your sibling
- Reverse the remaining slices to reorder them

Slicing is a powerful technique to extract a portion (a "slice") from a sequence. You take only the pieces you need without destroying the original pizza (the original data stays intact).

**Why slicing matters:**
- Extract specific portions of data without loops
- Manipulate sequences efficiently
- Create new sequences from existing ones
- Reverse sequences
- Step through data at intervals

---

## Basic Data Types

### 1. Integer (int)

#### What is an Integer? - The Counting Story

Imagine you're at a concert. You're counting the number of people in the audience:
- If you count 500 people, that's an integer
- If someone leaves, the count becomes 499 (still an integer)
- If it's below zero (like -5 degrees outside), that's still an integer

Integers are the most straightforward data type. An integer is a **whole number** - positive, negative, or zero. No decimal points, no fractions, no "approximately" - just pure, complete numbers.

**Why they matter:**
- Counting people at an event (you can't have 2.5 people)
- Tracking inventory (3 apples, not 3.2 apples)
- Age in complete years
- Number of attempts
- Scores in games

```python
age = 25              # How many complete years old you are
temperature = -5      # Degrees below zero
count = 0             # No items yet
people_in_room = 100  # You can't have a fraction of a person

print(type(age))  # Output: <class 'int'>
```

#### Integer Operations - Performing Magic with Numbers

Think of integer operations like magic tricks with numbers:

```python
# The Story: You have 10 apples and your friend has 3 apples
num1 = 10
num2 = 3

# Addition: Combining items
addition = num1 + num2  # 13 (total apples when combined)

# Subtraction: Taking away
subtraction = num1 - num2  # 7 (apples left if friend takes 3)

# Multiplication: Making copies
multiplication = num1 * num2  # 30 (if you triple the amount 3 times)

# Division: Sharing fairly
division = num1 / num2  # 3.333... (how many pieces if you split 10 into 3 parts)

# Floor Division: Fair sharing in whole pieces
floor_division = num1 // num2  # 3 (everyone gets 3 whole apples, 1 is left over)

# Modulus: What's left over
modulus = num1 % num2  # 1 (the 1 apple that couldn't be divided)

# Exponent: Multiplication power
exponent = num1 ** num2  # 1000 (10 × 10 × 10)

print(f"10 ÷ 3 = {division}")  # Output: 10 ÷ 3 = 3.333...
print(f"10 // 3 = {floor_division}")  # Output: 10 // 3 = 3
print(f"10 % 3 = {modulus}")  # Output: 10 % 3 = 1
```

**Practical example:** At a restaurant, you have 10 dollars and a meal costs 3 dollars.
- Floor division (10 // 3 = 3) tells you can buy 3 meals
- Modulus (10 % 3 = 1) tells you'll have 1 dollar left over

#### Integer Properties

```python
# Large numbers (no limit in Python!)
large_number = 999999999999999999999999999999
print(large_number)

# Binary, Octal, Hexadecimal
binary = 0b1010      # 10 in decimal
octal = 0o12         # 10 in decimal
hexadecimal = 0xA    # 10 in decimal

print(f"Binary 0b1010 = {binary}")        # Output: Binary 0b1010 = 10
print(f"Octal 0o12 = {octal}")            # Output: Octal 0o12 = 10
print(f"Hexadecimal 0xA = {hexadecimal}") # Output: Hexadecimal 0xA = 10
```

---

### 2. Float (float)

#### What is a Float? - The Precise Measurements Story

Imagine you're a scientist measuring the exact temperature of a chemical reaction. You can't just say "5 degrees" - you need to say "5.7 degrees" because precision matters for your experiment.

A float (floating-point number) is a number with a decimal point. It represents numbers that fall **between integers** - the precise, in-between values.

**Why floats matter:**
- Measuring exact amounts (5.5 liters of milk, not just 5)
- Temperature readings (98.6°F, not just 99°F)
- Financial calculations (prices: $19.99, not just $20)
- Scientific measurements (3.14159... for π)
- Percentages and ratios (0.85 meaning 85%)

**The name explanation:**
The decimal point "floats" - it can be in different positions:
- 19.99 (point near the end)
- 1.999 (point near the beginning)
- 0.0001 (point at the front)

```python
price = 19.99              # Amount you pay at a store
temperature = -5.5         # Precise temperature reading
pi = 3.14159               # Mathematical constant
average_score = 87.5       # Average of several test scores
probability = 0.75         # Likelihood of something happening (75%)

print(type(price))  # Output: <class 'float'>
```

#### Float Operations

```python
# Arithmetic operations (same as integers)
num1 = 10.5
num2 = 3.2

result = num1 + num2  # 13.7
result = num1 / num2  # 3.28125

print(result)  # Output: 3.28125
```

#### Special Float Values

```python
# Scientific notation
distance = 1.5e3      # 1500.0
tiny_value = 2.5e-3   # 0.0025

# Infinity and NaN (Not a Number)
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Infinity: {infinity}")
print(f"Negative Infinity: {negative_infinity}")
print(f"NaN: {not_a_number}")
```

#### Precision Issues (Important!)

```python
# Floating-point precision can be tricky
print(0.1 + 0.2)  # Output: 0.30000000000000004 (not exactly 0.3!)

# Solution: Use the decimal module for precise calculations
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(result)  # Output: 0.3
```

---

### 3. String (str)

#### What is a String? - The Message in a Bottle Story

Imagine you write a message on a piece of paper and put it in a bottle to send across the sea. The message might be:
- Short: "Help!"
- Long: "My name is Alex and I'm stranded on an island..."
- With symbols: "SOS!!! Please come!!!"

A string is exactly this - a **sequence of characters** (letters, numbers, symbols, spaces) all strung together and enclosed in quotes. Like pearls on a string, each character is connected to form a message.

**Why strings matter:**
- Storing names, addresses, descriptions
- Displaying messages to users
- Processing text data
- Creating labels and tags
- Storing any human-readable information

**Think of it this way:**
If numbers are like beads, strings are like beads on a thread - they're connected in a specific order, and that order matters. "Hello" is different from "olleH".

```python
name = "Alice"              # A single word
message = 'Hello, World!'   # A complete sentence
status = "Active"           # Status label
email = "alice@email.com"   # Email address
phone = "555-123-4567"      # Phone number with formatting

print(type(name))  # Output: <class 'str'>
```

**Important insight:**
Strings can contain numbers too, but they're treated as text:
- `"123"` is a string (three characters: 1, 2, 3)
- `123` is an integer (the number one hundred twenty-three)
- These behave completely differently!

#### String Creation

```python
# Different quote styles
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Multi
line
string'''

# Escape characters
escaped = "This is a \"quoted\" word"  # Output: This is a "quoted" word
tab_example = "Name\tAge\nAlice\t25"   # \t = tab, \n = newline
```

#### String Operations

```python
# Concatenation (joining)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# Repetition
laugh = "Ha" * 3
print(laugh)  # Output: HaHaHa

# String length
text = "Python"
length = len(text)
print(f"Length: {length}")  # Output: Length: 6
```

#### String Methods (Beginner Level)

```python
text = "  Hello Python World  "

# Case conversion
print(text.upper())        # Output: "  HELLO PYTHON WORLD  "
print(text.lower())        # Output: "  hello python world  "
print(text.capitalize())   # Output: "  hello python world  " (only first letter)
print(text.title())        # Output: "  Hello Python World  " (title case)

# Whitespace removal
print(text.strip())        # Output: "Hello Python World" (removes leading/trailing)
print(text.lstrip())       # Output: "Hello Python World  " (removes left side)
print(text.rstrip())       # Output: "  Hello Python World" (removes right side)

# Finding and replacing
greeting = "Hello World"
print(greeting.find("World"))      # Output: 6 (position of "World")
print(greeting.replace("World", "Python"))  # Output: "Hello Python"
print(greeting.count("l"))         # Output: 3 (count of "l")

# Checking content
print(greeting.startswith("Hello"))  # Output: True
print(greeting.endswith("World"))    # Output: True
print(greeting.isalpha())            # Output: False (contains space)
```

#### String Formatting (Important!)

```python
# Method 1: f-strings (modern, recommended)
name = "Alice"
age = 25
print(f"{name} is {age} years old")  # Output: Alice is 25 years old

# Method 2: format() method
print("{} is {} years old".format(name, age))  # Output: Alice is 25 years old

# Method 3: % operator (older style)
print("%s is %d years old" % (name, age))  # Output: Alice is 25 years old

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # Output: Price: $19.99
print(f"Percentage: {0.85*100:.1f}%")  # Output: Percentage: 85.0%
```

---

### 4. Boolean (bool)

#### What is a Boolean? - The Light Switch Story

Imagine a light switch in your room. It has only two states:
- **ON** (you can see everything)
- **OFF** (it's dark)

There's no "half-on" or "slightly-on" - it's either one or the other. This is exactly what a boolean is!

A boolean is the simplest data type - it can only be **`True`** or **`False`**. No in-between, no "maybe". It's binary - like yes or no, on or off, 1 or 0.

**Why booleans matter:**
- Making decisions in your code ("If it's raining, bring an umbrella")
- Checking conditions ("Is the user logged in?")
- Controlling program flow ("Should we continue or stop?")
- Storing yes/no information ("Is this a premium member?")

**Real-world examples:**
```python
is_student = True              # You ARE a student
is_raining = False             # It is NOT raining
has_valid_license = True       # License is valid
is_weekend = False             # Not a weekend (it's a weekday)
account_active = True          # Account is active

print(type(is_student))  # Output: <class 'bool'>
```

**Think of it like a checklist:**
- ✓ Door is locked? True
- ✗ Window is locked? False
- ✓ Stove is off? True
- ✗ Lights are off? False

#### Boolean Operations

```python
# Logical operations
print(True and True)      # Output: True
print(True and False)     # Output: False
print(True or False)      # Output: True
print(not True)           # Output: False

# Comparison operations (return booleans)
age = 20
print(age > 18)           # Output: True
print(age == 20)          # Output: True
print(age != 21)          # Output: True
```

#### Truthy and Falsy Values

In Python, values can be evaluated as `True` or `False`:

```python
# Falsy values (evaluate to False)
print(bool(0))            # Output: False
print(bool(0.0))          # Output: False
print(bool(""))           # Output: False (empty string)
print(bool([]))           # Output: False (empty list)
print(bool(None))         # Output: False

# Truthy values (evaluate to True)
print(bool(1))            # Output: True
print(bool("text"))       # Output: True (non-empty string)
print(bool([1, 2, 3]))    # Output: True (non-empty list)

# Practical use
text = input("Enter something: ")
if text:  # If text is not empty (truthy)
    print("You entered something!")
```

---

### 5. None (NoneType)

#### What is None?

`None` is a special value that represents the absence of a value. It's Python's way of saying "nothing".

```python
result = None
print(type(result))  # Output: <class 'NoneType'>

# Common uses
user_input = None  # Default value
if user_input is None:
    print("No input provided")
```

---

## Collection Data Types

Collection data types store multiple values. The main ones are: **lists, tuples, dictionaries, and sets**.

### 6. List (list)

#### What is a List?

A list is an ordered, mutable collection. You can add, remove, and change items. Lists are enclosed in square brackets `[]`.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Lists can contain different types!

print(type(fruits))  # Output: <class 'list'>
```

#### Accessing List Elements

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# By index (position) - remember, Python starts counting from 0!
print(fruits[0])      # Output: "apple"
print(fruits[1])      # Output: "banana"
print(fruits[-1])     # Output: "elderberry" (last item)
print(fruits[-2])     # Output: "date" (second-to-last)

# Index visualization:
# Index:    0       1        2       3      4
# Value:  apple  banana   cherry  date  elderberry
# Negative: -5    -4       -3     -2    -1
```

#### List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Adding elements
numbers.append(5)           # Add to end: [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers.insert(0, 10)       # Insert at position 0: [10, 3, 1, 4, ...]
numbers.extend([7, 8])      # Add multiple items: [..., 6, 5, 7, 8]

# Removing elements
numbers.remove(3)           # Remove first occurrence of 3
numbers.pop()               # Remove and return last item
numbers.pop(0)              # Remove and return item at index 0
numbers.clear()             # Remove all items

# Finding and counting
original = [3, 1, 4, 1, 5, 9, 2, 6]
index = original.index(4)   # Output: 2 (position of 4)
count = original.count(1)   # Output: 2 (how many 1s)

# Sorting and reversing
numbers = [3, 1, 4, 1, 5]
numbers.sort()              # Sort in place: [1, 1, 3, 4, 5]
numbers.reverse()           # Reverse in place: [5, 4, 3, 1, 1]

# Creating new sorted/reversed lists
numbers = [3, 1, 4, 1, 5]
sorted_list = sorted(numbers)      # [1, 1, 3, 4, 5] (new list)
reversed_list = list(reversed(numbers))  # [5, 1, 4, 1, 3] (new list)
```

#### List Comprehension

```python
# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# With conditions - only even numbers
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # Output: [4, 16, 36, 64, 100]
```

---

### 7. Tuple (tuple)

#### What is a Tuple?

A tuple is similar to a list, but **immutable** - you cannot change, add, or remove items after creation. Enclosed in parentheses `()`.

**Why use tuples?**
- Protect data from accidental modification
- Use as dictionary keys
- Faster than lists for large collections
- Unpack multiple values easily

```python
colors = ("red", "green", "blue")
coordinates = (10, 20)
single_item = (42,)  # Note the comma! Without it, it's just the number 42

print(type(colors))  # Output: <class 'tuple'>
```

#### Accessing Tuple Elements

```python
colors = ("red", "green", "blue", "yellow")

# Same indexing as lists
print(colors[0])      # Output: "red"
print(colors[-1])     # Output: "yellow"
print(len(colors))    # Output: 4
```

#### Tuple Operations

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 2
print(repeated)  # Output: (1, 2, 3, 1, 2, 3)

# Unpacking
red, green, blue = ("red", "green", "blue")
print(red)    # Output: "red"
print(green)  # Output: "green"

# Methods (limited compared to lists)
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))     # Output: 3 (count of 2s)
print(numbers.index(3))     # Output: 2 (position of first 3)
```

---

### 8. Dictionary (dict)

#### What is a Dictionary?

A dictionary stores data in **key-value pairs**. Like a real dictionary - you look up a word (key) to get its definition (value).

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "gpa": 3.8
}

print(type(student))  # Output: <class 'dict'>
```

#### Accessing Dictionary Values

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Access by key
print(student["name"])      # Output: "Alice"
print(student["age"])       # Output: 20

# Safe access with get()
print(student.get("name"))  # Output: "Alice"
print(student.get("city"))  # Output: None (key doesn't exist)
print(student.get("city", "Unknown"))  # Output: "Unknown" (default value)
```

#### Dictionary Operations

```python
student = {"name": "Alice", "age": 20}

# Adding/updating items
student["grade"] = "A"      # Add new key-value pair
student["age"] = 21         # Update existing value

print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

# Removing items
del student["grade"]        # Delete a key-value pair
student.pop("age")          # Remove and return value
student.clear()             # Remove all items

# Dictionary methods
student = {"name": "Alice", "age": 20, "grade": "A"}

keys = student.keys()           # Get all keys
values = student.values()       # Get all values
items = student.items()         # Get key-value pairs

print(list(keys))    # Output: ['name', 'age', 'grade']
print(list(values))  # Output: ['Alice', 20, 'A']
print(list(items))   # Output: [('name', 'Alice'), ('age', 20), ('grade', 'A')]

# Check existence
print("name" in student)    # Output: True
print("city" in student)    # Output: False
```

#### Dictionary Comprehension

```python
# Create a dictionary of squares
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With conditions
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

#### Iterating Through Dictionaries

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# Iterate over keys
for key in student:
    print(key)  # Output: name, age, grade

# Iterate over values
for value in student.values():
    print(value)  # Output: Alice, 20, A

# Iterate over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
    # Output: name: Alice
    #         age: 20
    #         grade: A
```

---

### 9. Set (set)

#### What is a Set?

A set is an unordered collection of **unique items**. No duplicates allowed. Useful for removing duplicates and checking membership.

```python
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4, 5}

print(type(colors))  # Output: <class 'set'>
print(len(colors))   # Output: 3
```

#### Set Operations

```python
# Creating a set
unique_numbers = {1, 2, 2, 3, 3, 3}
print(unique_numbers)  # Output: {1, 2, 3} (duplicates removed!)

# Adding and removing
colors = {"red", "green"}
colors.add("blue")          # Add one item
colors.update(["yellow"])   # Add multiple items
colors.remove("red")        # Remove (error if not found)
colors.discard("red")       # Remove (no error if not found)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2              # {1, 2, 3, 4, 5, 6} (all items)
intersection = set1 & set2       # {3, 4} (common items)
difference = set1 - set2         # {1, 2} (in set1 but not set2)
symmetric_difference = set1 ^ set2  # {1, 2, 5, 6} (in either but not both)

print(union)
print(intersection)
print(difference)
```

#### Set Comprehension

```python
# Create a set of unique squares
squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}
```

---

## Understanding Slicing

### What is Slicing?

Slicing extracts a portion (a "slice") from a sequence. It creates a new sequence without modifying the original.

**Syntax:**
```
sequence[start:stop:step]
```

- **start**: Beginning index (inclusive) - default is 0
- **stop**: Ending index (exclusive) - default is length of sequence
- **step**: Interval between items - default is 1

### 10. String Slicing (Beginner)

#### Basic String Slicing

```python
text = "Hello World"
#      0123456789(10)
# Indices: H=0, e=1, l=2, l=3, o=4, space=5, W=6, ...

# Get character at position
print(text[0])      # Output: "H"
print(text[6])      # Output: "W"

# Slice from start to position (not including position)
print(text[0:5])    # Output: "Hello"
print(text[6:11])   # Output: "World"

# Slice from position to end
print(text[6:])     # Output: "World"

# Slice from start to position
print(text[:5])     # Output: "Hello"

# Slice entire string
print(text[:])      # Output: "Hello World"
```

#### Negative Indexing in Strings

```python
text = "Python"
#       012345 (forward)
#      -654-3-2-1 (backward)

print(text[-1])     # Output: "n" (last character)
print(text[-2])     # Output: "o" (second-to-last)
print(text[-4:])    # Output: "hon" (last 4 characters)
print(text[:-1])    # Output: "Pytho" (all except last)
print(text[-4:-1])  # Output: "tho" (from -4 to -1, not including -1)
```

#### Step in String Slicing

```python
text = "Python"

# Every 2nd character
print(text[::2])    # Output: "Pto"

# Every 3rd character
print(text[::3])    # Output: "Pn"

# Reverse string (step -1)
print(text[::-1])   # Output: "nohtyP"

# Every 2nd character in reverse
print(text[::-2])   # Output: "noP"
```

#### Real-World Examples: String Slicing

```python
# Extract area code from phone number
phone = "555-123-4567"
area_code = phone[0:3]
print(area_code)  # Output: "555"

# Get file extension
filename = "document.pdf"
extension = filename[-4:]
print(extension)  # Output: ".pdf"

# Extract date components
date_string = "2024-12-25"
year = date_string[0:4]
month = date_string[5:7]
day = date_string[8:10]
print(f"Year: {year}, Month: {month}, Day: {day}")

# Remove whitespace (clever slice trick)
text = "  hello  "
trimmed = text[1:-1]  # Removes first and last character
print(f"'{trimmed}'")  # Output: ' hello '
```

---

### 11. List Slicing (Beginner to Intermediate)

#### Basic List Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract portion
print(numbers[2:5])     # Output: [2, 3, 4]
print(numbers[0:3])     # Output: [0, 1, 2]
print(numbers[5:])      # Output: [5, 6, 7, 8, 9]
print(numbers[:5])      # Output: [0, 1, 2, 3, 4]
print(numbers[:])       # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### List Slicing with Step

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every 2nd element
print(numbers[::2])     # Output: [0, 2, 4, 6, 8]

# Every 3rd element
print(numbers[::3])     # Output: [0, 3, 6, 9]

# Every 2nd element starting from index 1
print(numbers[1::2])    # Output: [1, 3, 5, 7, 9]

# Reverse list
print(numbers[::-1])    # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Reverse every 2nd element
print(numbers[::-2])    # Output: [9, 7, 5, 3, 1]
```

#### Negative Indexing in Lists

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[-1])       # Output: "elderberry"
print(fruits[-3:])      # Output: ["cherry", "date", "elderberry"]
print(fruits[:-2])      # Output: ["apple", "banana", "cherry"]
print(fruits[-4:-1])    # Output: ["banana", "cherry", "date"]
```

#### List Slicing Creates New Lists

**Important:** Slicing creates a new list; it doesn't modify the original.

```python
original = [1, 2, 3, 4, 5]
sliced = original[1:4]  # [2, 3, 4]

# Modify the slice
sliced[0] = 99

print(original)  # Output: [1, 2, 3, 4, 5] (unchanged)
print(sliced)    # Output: [99, 3, 4]
```

---

### 12. Tuple Slicing (Beginner)

#### Tuple Slicing

Tuples use the same slicing syntax as lists. Remember, tuples are immutable!

```python
coordinates = (10, 20, 30, 40, 50)

print(coordinates[1:4])     # Output: (20, 30, 40)
print(coordinates[::2])     # Output: (10, 30, 50)
print(coordinates[::-1])    # Output: (50, 40, 30, 20, 10)
```

---

## Advanced Slicing Techniques

### 13. Extended Slicing (Intermediate to Advanced)

#### Slice Assignment (Lists Only)

Slices can be assigned new values to modify lists in place.

```python
numbers = [1, 2, 3, 4, 5]

# Replace a slice with new values
numbers[1:4] = [20, 30, 40]
print(numbers)  # Output: [1, 20, 30, 40, 5]

# Replace with different-length list
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30, 40, 50]  # 2 elements replaced with 4
print(numbers)  # Output: [1, 20, 30, 40, 50, 4, 5]

# Delete a slice
numbers = [1, 2, 3, 4, 5]
del numbers[1:4]
print(numbers)  # Output: [1, 5]

# Insert without replacing
numbers = [1, 2, 3, 4, 5]
numbers[2:2] = [99, 88]  # Insert at position 2
print(numbers)  # Output: [1, 2, 99, 88, 3, 4, 5]

# Delete using slice assignment
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []  # Remove elements
print(numbers)  # Output: [1, 5]
```

#### Advanced Step Slicing

```python
# Reverse a specific range
text = "abcdefghij"
print(text[8:2:-1])  # Output: "ihgfed" (from index 8 to 2, stepping backward)

# Complex slicing
numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[8:2:3])      # Output: [8, 5] (from 8 to 2, step 3)
```

---

### 14. slice() Object (Advanced)

Python provides a `slice()` object for complex slicing operations.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a slice object
s = slice(2, 7, 2)  # start=2, stop=7, step=2

result = numbers[s]
print(result)  # Output: [2, 4, 6]

# Equivalent to
print(numbers[2:7:2])  # Output: [2, 4, 6]

# Useful for storing and reusing slice patterns
slice_first_three = slice(None, 3)      # [:][:3]
slice_last_three = slice(-3, None)      # [-3:]
slice_every_other = slice(None, None, 2)  # [::2]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[slice_first_three])      # Output: ['apple', 'banana', 'cherry']
print(fruits[slice_last_three])       # Output: ['date', 'elderberry']
print(fruits[slice_every_other])      # Output: ['apple', 'cherry', 'elderberry']
```

---

### 15. Slicing with Strings (Advanced Techniques)

#### Multi-line String Slicing

```python
poem = """Roses are red
Violets are blue
Sugar is sweet
And so are you"""

# Get lines using find or split
lines = poem.split('\n')
print(lines[0])  # Output: "Roses are red"
print(lines[1])  # Output: "Violets are blue"
```

#### Pattern Extraction with Slicing

```python
# Extract initials from a name
name = "John Michael Smith"
initials = ''.join([word[0] for word in name.split()])
print(initials)  # Output: "JMS"

# Extract words of specific lengths
sentence = "The quick brown fox jumps"
words = sentence.split()
long_words = [word for word in words if len(word) > 4]
print(long_words)  # Output: ['quick', 'brown', 'jumps']
```

---

## Practical Applications

### Application 1: Data Validation

```python
def validate_email(email):
    """Check if email has valid format using slicing and methods"""
    if '@' not in email:
        return False
    
    at_index = email.find('@')
    local_part = email[:at_index]  # Everything before @
    domain_part = email[at_index+1:]  # Everything after @
    
    # Check if both parts are non-empty
    return len(local_part) > 0 and len(domain_part) > 0

print(validate_email("user@example.com"))  # Output: True
print(validate_email("invalid.email"))     # Output: False
```

### Application 2: String Parsing

```python
# Parse a CSV-like string
data = "John,25,Engineer,New York"
values = data.split(',')

name = values[0]
age = int(values[1])
job = values[2]
city = values[3]

print(f"{name} is {age} and works as a {job} in {city}")

# Alternative using slicing
fields = data.split(',')
name, age = fields[0], int(fields[1])  # Using slicing
print(f"{name} is {age}")
```

### Application 3: Text Manipulation

```python
def reverse_words(sentence):
    """Reverse the order of words in a sentence"""
    words = sentence.split()
    reversed_words = words[::-1]  # Slice with step -1
    return ' '.join(reversed_words)

result = reverse_words("Hello World from Python")
print(result)  # Output: "Python from World Hello"
```

### Application 4: List Processing

```python
# Extract data in chunks
numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]

# Split into groups of 3
chunk_size = 3
chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
print(chunks)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
```

### Application 5: Matrix/Grid Operations

```python
# Simple 2D list operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get first row
first_row = matrix[0]
print(first_row)  # Output: [1, 2, 3]

# Get first column (using list comprehension with slicing)
first_column = [row[0] for row in matrix]
print(first_column)  # Output: [1, 4, 7]

# Reverse rows
reversed_matrix = matrix[::-1]
print(reversed_matrix)  # Output: [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
```

### Application 6: Password/Token Masking

```python
def mask_password(password):
    """Show only first and last character of password"""
    if len(password) <= 2:
        return "*" * len(password)
    
    first = password[0]
    last = password[-1]
    middle = "*" * (len(password) - 2)
    
    return first + middle + last

print(mask_password("secret123"))  # Output: s*********3
print(mask_password("pass"))       # Output: p**s
```

### Application 7: Time/Date Manipulation

```python
# Parse and extract time components
time_string = "14:35:42"
hours = time_string[0:2]
minutes = time_string[3:5]
seconds = time_string[6:8]

print(f"Time: {hours}h {minutes}m {seconds}s")  # Output: Time: 14h 35m 42s

# Format time (reverse technique)
formatted_time = f"{hours}:{minutes}:{seconds}"
print(formatted_time)  # Output: 14:35:42
```

---

## Performance Tips

### Memory Efficiency

```python
# Slicing creates a new object (uses memory)
large_list = list(range(1000000))
slice_copy = large_list[100:200]  # Creates new list with 100 items

# For large operations, consider itertools
from itertools import islice

# Get items without creating full list copy (lazy evaluation)
first_100 = list(islice(large_list, 100))
items_100_to_200 = list(islice(large_list, 100, 200))
```

### Time Complexity

```python
# Slicing is O(k) where k is size of slice
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice1 = items[0:3]      # O(3) - fast, small slice
slice2 = items[0:1000]   # O(10) - copies entire list

# For membership testing, use sets (O(1)) instead of lists (O(n))
small_list = [1, 2, 3, 4, 5]
small_set = {1, 2, 3, 4, 5}

print(3 in small_list)   # O(n) - slower for lists
print(3 in small_set)    # O(1) - faster for sets
```

---

## Best Practices

### 1. Be Clear with Slice Intent

❌ **Bad:**
```python
result = data[1:10:2]  # What does this do? Not clear!
```

✅ **Good:**
```python
# Extract every other item from index 1 to 10
skip_index = slice(1, 10, 2)
result = data[skip_index]

# Or add a comment explaining the slice
result = data[1:10:2]  # Get elements at odd indices from 1-9
```

### 2. Handle Index Out of Bounds

```python
# Slicing is safe - doesn't raise errors for out-of-bounds indices
text = "Hello"
print(text[0:100])      # Output: "Hello" (safe, doesn't error)
print(text[100:200])    # Output: "" (empty string)

# But indexing can raise errors
# print(text[100])      # IndexError!
```

### 3. Remember: Slicing Excludes the Stop Index

```python
items = ["a", "b", "c", "d", "e"]

# Common mistake
print(items[1:3])      # Output: ["b", "c"] NOT ["b", "c", "d"]
#                      Stop index 3 is NOT included

# To include index 3, use stop = 4
print(items[1:4])      # Output: ["b", "c", "d"]
```

### 4. Use Slice Assignment Carefully (Lists Only)

```python
# Strings and tuples don't support slice assignment
text = "hello"
# text[0:2] = "HE"  # TypeError! Can't assign to string slice

# Lists do support it
numbers = [1, 2, 3, 4, 5]
numbers[0:2] = [10, 20]  # Works fine
print(numbers)  # Output: [10, 20, 3, 4, 5]
```

### 5. Understand Mutable vs Immutable

```python
# String (immutable) - slicing creates new string
text1 = "Hello"
text2 = text1[:]
text2 = "World"  # Creates new string
print(text1)  # Output: "Hello" (unchanged)

# List (mutable) - slicing creates new list, but elements may be shared
list1 = [[1, 2], [3, 4]]
list2 = list1[:]  # Shallow copy
list2[0][0] = 99
print(list1)  # Output: [[99, 2], [3, 4]] (changed!)

# Use deepcopy for nested structures
import copy
list3 = copy.deepcopy(list1)
list3[0][0] = 100
print(list1)  # Output: [[99, 2], [3, 4]] (unchanged!)
```

### 6. Use Appropriate Data Structures

```python
# For extracting consecutive elements - use slicing
data = [1, 2, 3, 4, 5]
consecutive = data[1:4]  # Good

# For extracting non-consecutive elements - use indexing or comprehension
indices = [0, 2, 4]
non_consecutive = [data[i] for i in indices]  # Better than slicing
```

---

## Quick Reference Cheat Sheet

### Data Types Summary

| Type | Syntax | Mutable | Duplicates | Ordered |
|------|--------|---------|-----------|---------|
| **list** | `[1, 2, 3]` | Yes | Yes | Yes |
| **tuple** | `(1, 2, 3)` | No | Yes | Yes |
| **set** | `{1, 2, 3}` | Yes | No | No |
| **dict** | `{"a": 1}` | Yes | Keys unique | Yes (3.7+) |
| **str** | `"hello"` | No | Yes | Yes |

### Slicing Syntax Reference

```
sequence[start:stop:step]
```

| Syntax | Result | Example |
|--------|--------|---------|
| `[:]` | Entire sequence | `[1,2,3]` |
| `[n:]` | From index n to end | `[2,3,4,5]` |
| `[:n]` | From start to index n | `[1,2,3]` |
| `[n:m]` | From index n to m | `[2,3,4]` |
| `[::k]` | Every k-th element | `[1,3,5]` (k=2) |
| `[::-1]` | Reversed sequence | `[5,4,3,2,1]` |
| `[-n:]` | Last n elements | `[4,5]` (n=2) |
| `[:-n]` | All except last n | `[1,2,3]` (n=2) |

---

## Conclusion

Understanding Python's data types and slicing techniques is fundamental to becoming proficient in Python programming. These concepts allow you to:

- **Store and organize data** efficiently
- **Extract information** from sequences quickly
- **Manipulate data** with minimal code
- **Write cleaner, more readable** programs
- **Process large datasets** effectively

Practice these concepts regularly with different data types and slicing patterns to build mastery!

---

## Practice Exercises

### Easy Level

1. Create a list of numbers 1-10 and slice to get the first 5 elements
2. Create a string and reverse it using slicing
3. Extract the last 3 elements from a list
4. Check if a set has any duplicate elements

### Medium Level

5. Parse a date string "2024-12-25" using slicing to extract year, month, day
6. Create a function that returns every other element from a list
7. Given a list, slice it into chunks of size 3
8. Remove duplicates from a list using a set

### Hard Level

9. Write a function that implements Caesar cipher using string slicing
10. Create a function to transpose a 2D list (matrix transpose)
11. Implement a function to find all overlapping substrings of length k
12. Parse and validate a credit card number format using slicing

---



