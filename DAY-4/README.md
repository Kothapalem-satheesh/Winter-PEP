# Python Conditionals and Loops: Complete Guide
## From Basics to Advanced Concepts

### Table of Contents
1. [Introduction](#introduction)
2. [Basic Conditional Statements](#basic-conditional-statements)
3. [Advanced Conditional Patterns](#advanced-conditional-patterns)
4. [Basic Loops](#basic-loops)
5. [Advanced Loop Techniques](#advanced-loop-techniques)
6. [Nested Structures](#nested-structures)
7. [Loop Control Statements](#loop-control-statements)
8. [Comprehensions](#comprehensions)
9. [Advanced Patterns and Best Practices](#advanced-patterns-and-best-practices)
10. [Real-World Examples](#real-world-examples)
11. [Performance Considerations](#performance-considerations)
12. [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)

---

## Introduction

This comprehensive guide covers Python's conditional statements and loops from basic concepts to advanced techniques. Whether you're a beginner or looking to master advanced patterns, this guide provides practical examples and best practices.

### Prerequisites
- Basic Python syntax knowledge
- Understanding of variables and data types
- Familiarity with Python operators

---

## Basic Conditional Statements

### 1. The if Statement

The `if` statement is the foundation of conditional logic in Python.

```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# Example with user input
name = input("Enter your name: ")
if name:
    print(f"Hello, {name}!")
```

### 2. The if-else Statement

```python
# Basic if-else
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# Example with boolean conditions
is_raining = True
if is_raining:
    print("Take an umbrella")
else:
    print("No need for an umbrella")
```


# Python Conditionals and Loops: Comprehensive Guide

## Overview
This guide covers Python conditionals and loops from basic to advanced concepts with practical examples.

## Part 1: Basic Conditionals

### Simple if Statements
```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot")

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")
```

### Comparison Operators
```python
x, y = 10, 20
print(f"{x} == {y}: {x == y}")  # Equal
print(f"{x} != {y}: {x != y}")  # Not equal
print(f"{x} < {y}: {x < y}")    # Less than
print(f"{x} <= {y}: {x <= y}")  # Less or equal
print(f"{x} > {y}: {x > y}")    # Greater than
print(f"{x} >= {y}: {x >= y}")  # Greater or equal

# Chained comparisons
num = 15
if 10 < num < 20:
    print("Number is between 10 and 20")
```

### Logical Operators
```python
# AND operator
age = 25
has_license = True
if age >= 18 and has_license:
    print("Can drive")

# OR operator
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("No work today!")

# NOT operator
is_raining = False
if not is_raining:
    print("Good day for a walk")
```

## Part 2: Advanced Conditionals

### Ternary Operator
```python
# Basic ternary
age = 20
status = "adult" if age >= 18 else "minor"

# Nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"

# In list comprehensions
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
```

### Match-Case (Python 3.10+)
```python
def handle_status(code):
    match code:
        case 200:
            return "Success"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown"

# Pattern matching with data
def process_data(data):
    match data:
        case {"type": "user", "name": str(name)}:
            return f"User: {name}"
        case [first, *rest]:
            return f"List: {first} + {len(rest)} more"
        case _:
            return "Unknown format"
```

## Part 3: Basic Loops

### For Loops
```python
# Range loops
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Iterating sequences
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Dictionary iteration
person = {"name": "John", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# Enumerate for index + value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

### While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Input validation
while True:
    age = input("Enter age: ")
    if age.isdigit() and int(age) > 0:
        break
    print("Invalid input!")

# Game loop
import random
secret = random.randint(1, 10)
attempts = 0

while attempts < 3:
    guess = int(input("Guess (1-10): "))
    attempts += 1
    
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

## Part 4: Advanced Loop Techniques

### Nested Loops
```python
# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2d}", end=" ")
    print()

# Pattern printing
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

### Loop Control
```python
# Break and continue
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(i)

# Loop-else clause
for i in range(5):
    if i == 10:  # Never true
        break
else:
    print("Loop completed normally")

# Prime checker
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return n > 1
```

## Part 5: Comprehensions

### List Comprehensions
```python
# Basic comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# With if-else
labels = ["pos" if x > 0 else "neg" for x in [-1, 2, -3, 4]]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]

# Flattening
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in nested for x in row]
```

### Dictionary and Set Comprehensions
```python
# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
word_lens = {word: len(word) for word in ["hi", "hello"]}

# Set comprehension
unique_chars = {c.lower() for c in "Hello World" if c.isalpha()}

# Generator expression
squares_gen = (x**2 for x in range(1000))
sum_squares = sum(x**2 for x in range(100))
```

This guide provides a solid foundation for understanding Python conditionals and loops. Each section builds upon the previous one, progressing from basic concepts to advanced techniques with practical examples.
