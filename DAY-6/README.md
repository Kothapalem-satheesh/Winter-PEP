# DAY-6 Object-Oriented Programming (OOP) 
## From Beginner to Advanced 

---

## 📑 Table of Contents
1. [Introduction to OOP](#introduction-to-oop)
2. [Classes and Objects](#classes-and-objects)
3. [Attributes and Methods](#attributes-and-methods)
4. [Constructors and Initialization](#constructors-and-initialization)
5. [Encapsulation](#encapsulation)
6. [Inheritance](#inheritance)
7. [Polymorphism](#polymorphism)
8. [Abstraction](#abstraction)
9. [Special Methods (Dunder Methods)](#special-methods-dunder-methods)
10. [Class vs Instance Variables](#class-vs-instance-variables)
11. [Static and Class Methods](#static-and-class-methods)
12. [Properties and Decorators](#properties-and-decorators)
13. [Composition](#composition)
14. [Advanced OOP Concepts](#advanced-oop-concepts)
15. [Design Patterns](#design-patterns)
16. [Practical Applications](#practical-applications)
17. [Best Practices](#best-practices)

---

## Introduction to OOP

### What is Object-Oriented Programming? - The Restaurant Story 🍽️

Imagine you're opening a restaurant. In real life, you need to think about different things:

```
┌─────────────────────────────────────────────────┐
│           THE RESTAURANT                        │
├─────────────────────────────────────────────────┤
│                                                 │
│  🍽️  OBJECT: Chef "Alice"                      │
│      Attributes:                                │
│      • Name: Alice                              │
│      • Experience: 10 years                     │
│      • Specialty: Italian Cuisine               │
│                                                 │
│      Methods:                                   │
│      • cook_pasta()                             │
│      • make_sauce()                             │
│      • taste_food()                             │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  🍴 OBJECT: Dish "Pasta Carbonara"             │
│      Attributes:                                │
│      • Name: Pasta Carbonara                    │
│      • Price: $15                               │
│      • Calories: 450                            │
│                                                 │
│      Methods:                                   │
│      • serve()                                  │
│      • get_price()                              │
│      • is_vegetarian()                          │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Object-Oriented Programming (OOP)** is about organizing your code by creating **objects** that represent real-world things.

Instead of writing procedures that do things, you create objects that:
- **Have properties** (attributes) - like name, age, color
- **Can do things** (methods) - like walk(), eat(), sleep()

**Why OOP Matters:**
- 🏗️ **Real-world modeling**: Code mirrors reality
- 🔄 **Reusability**: Create once, reuse everywhere
- 🛡️ **Maintainability**: Changes are isolated
- 📦 **Organization**: Related code stays together
- 🎯 **Scalability**: Easier to build large programs
- 🧩 **Modularity**: Break problems into pieces

---

## Classes and Objects

### Understanding Classes vs Objects 🎯

A **class** is a blueprint or template. An **object** is an actual instance created from that blueprint.

```
┌─────────────────────────────────────┐
│   BLUEPRINT vs ACTUAL ITEM          │
├─────────────────────────────────────┤
│                                     │
│  CLASS: Cookie Recipe               │
│  ────────────────────────────────   │
│  A piece of paper with              │
│  instructions to make cookies       │
│                                     │
│  OBJECT: Actual Cookie              │
│  ────────────────────────────────   │
│  A real cookie you can eat!         │
│  Made from the recipe               │
│                                     │
│  One recipe → Many cookies!         │
│                                     │
└─────────────────────────────────────┘
```

### Creating Your First Class

```python
# STEP 1: Define the class (blueprint)
class Person:
    """A class representing a person"""
    pass  # Will add details soon

# STEP 2: Create objects (instances)
alice = Person()   # Create object 1
bob = Person()     # Create object 2

print(type(alice))  # Output: <class '__main__.Person'>
print(type(bob))    # Output: <class '__main__.Person'>

# Both alice and bob are instances of Person class
```

### A Real Example: Car Class

```python
class Car:
    """A class representing a car"""
    
    # Attributes (properties)
    brand = "Toyota"
    color = "Red"
    year = 2024
    speed = 0

# Create car objects
my_car = Car()
print(my_car.brand)  # Output: Toyota
print(my_car.color)  # Output: Red
print(my_car.year)   # Output: 2024

# Create another car
friend_car = Car()
print(friend_car.brand)  # Output: Toyota (same class, same values)
```

**Visual Representation:**

```
┌──────────────────────────────────────┐
│      CLASS: Car (Blueprint)          │
├──────────────────────────────────────┤
│  Attributes:                         │
│  • brand                             │
│  • color                             │
│  • year                              │
│  • speed                             │
└──────────────────────────────────────┘
         ↓ (creates)
    ┌────────┬────────┐
    ↓        ↓        ↓
  my_car  friend_car other_car
  (object) (object)  (object)
```

---

## Attributes and Methods

### Attributes - Properties of Objects 📋

Attributes are variables that belong to an object:

```python
class Dog:
    """A class representing a dog"""
    
    # Class attributes (shared by all dogs)
    species = "Canis familiaris"
    
    # We'll set instance attributes later in __init__

# Create a dog object
my_dog = Dog()
print(my_dog.species)  # Output: Canis familiaris

# Set instance attributes directly
my_dog.name = "Buddy"
my_dog.age = 3
my_dog.color = "Golden"

print(my_dog.name)   # Output: Buddy
print(my_dog.age)    # Output: 3
print(my_dog.color)  # Output: Golden
```

### Methods - Actions Objects Can Perform 🎬

Methods are functions that belong to a class:

```python
class Dog:
    """A dog class with methods"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says: Woof! Woof!"
    
    def get_age(self):
        """Return the dog's age"""
        return f"{self.name} is {self.age} years old"
    
    def have_birthday(self):
        """Increase the dog's age"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old"

# Create and use
buddy = Dog("Buddy", 3)

print(buddy.bark())              # Output: Buddy says: Woof! Woof!
print(buddy.get_age())           # Output: Buddy is 3 years old
print(buddy.have_birthday())     # Output: Happy birthday! Buddy is now 4 years old
```

**Understanding `self` Parameter:**

The `self` parameter refers to the object itself. It's how the object accesses its own attributes:

```python
class Person:
    def __init__(self, name):
        self.name = name  # self.name = this person's name
    
    def greet(self):
        return f"Hello, I'm {self.name}"  # self.name = this person's name

alice = Person("Alice")
print(alice.greet())  # Output: Hello, I'm Alice

bob = Person("Bob")
print(bob.greet())    # Output: Hello, I'm Bob

# Each object has its own self!
```

---

## Constructors and Initialization

### The __init__ Method - Constructor Story 🏗️

The `__init__` method is a **constructor**. It runs automatically when you create a new object:

```
┌─────────────────────────────────────┐
│   CREATING A NEW OBJECT             │
├─────────────────────────────────────┤
│                                     │
│  alice = Person("Alice", 25)        │
│     ↓                               │
│  __init__ is called AUTOMATICALLY   │
│     ↓                               │
│  self.name = "Alice"                │
│  self.age = 25                      │
│     ↓                               │
│  alice object is ready to use!      │
│                                     │
└─────────────────────────────────────┘
```

### Constructor Example

```python
class Person:
    """A person with name and age"""
    
    def __init__(self, name, age):
        """Initialize a person"""
        self.name = name
        self.age = age
        self.created_at = "2024"
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

# Creating objects
alice = Person("Alice", 25)
bob = Person("Bob", 30)

print(alice.introduce())  # Output: Hi, I'm Alice and I'm 25 years old
print(bob.introduce())    # Output: Hi, I'm Bob and I'm 30 years old

# Each object has its own attributes
print(alice.name)  # Output: Alice
print(bob.name)    # Output: Bob
```

### Constructor with Default Values

```python
class Car:
    """A car with default values"""
    
    def __init__(self, brand, year=2024, color="White"):
        """
        Initialize a car
        
        Args:
            brand (str): Car brand (required)
            year (int): Year of manufacture (default: 2024)
            color (str): Car color (default: White)
        """
        self.brand = brand
        self.year = year
        self.color = color
    
    def describe(self):
        return f"{self.color} {self.year} {self.brand}"

# Create cars with different parameters
car1 = Car("Toyota")
print(car1.describe())  # Output: White 2024 Toyota

car2 = Car("BMW", 2023)
print(car2.describe())  # Output: White 2023 BMW

car3 = Car("Ferrari", 2024, "Red")
print(car3.describe())  # Output: Red 2024 Ferrari
```

---

## Encapsulation

### What is Encapsulation? - The Bank Account Story 🏦

Encapsulation means hiding internal details and controlling how data is accessed. Think of a bank account:

```
┌─────────────────────────────────────────┐
│        BANK ACCOUNT                     │
├─────────────────────────────────────────┤
│                                         │
│  PRIVATE (Hidden from outside):         │
│  • Internal ledger                      │
│  • Transaction logs                     │
│  • Security codes                       │
│                                         │
│  PUBLIC (What you can do):              │
│  • deposit(amount)                      │
│  • withdraw(amount)                     │
│  • check_balance()                      │
│                                         │
│  You can't directly touch the money!    │
│  You must use the provided methods!     │
│                                         │
└─────────────────────────────────────────┘
```

### Private and Public Attributes

```python
class BankAccount:
    """A bank account with encapsulation"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # _ means "private" (convention)
    
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Cannot deposit negative amount"
    
    def withdraw(self, amount):
        """Remove money from account"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    def check_balance(self):
        """Check account balance"""
        return f"Balance: ${self._balance}"

# Use the account
account = BankAccount("Alice", 1000)

print(account.deposit(500))      # Output: Deposited $500. New balance: $1500
print(account.withdraw(200))     # Output: Withdrew $200. New balance: $1300
print(account.check_balance())   # Output: Balance: $1300

# ❌ Don't do this (breaks encapsulation):
# account._balance = -5000  # Bad! Hides the business logic
```

### Using Property Decorators for Encapsulation

```python
class Student:
    """A student with protected GPA"""
    
    def __init__(self, name, gpa=0.0):
        self.name = name
        self._gpa = gpa  # Private attribute
    
    @property
    def gpa(self):
        """Get the GPA (read-only)"""
        return round(self._gpa, 2)
    
    @gpa.setter
    def gpa(self, value):
        """Set the GPA with validation"""
        if 0.0 <= value <= 4.0:
            self._gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

# Use the student
student = Student("Bob", 3.5)

print(student.gpa)      # Output: 3.5 (getter is called)
student.gpa = 3.8       # Setter is called with validation
print(student.gpa)      # Output: 3.8

# This will raise an error (validation)
# student.gpa = 5.0  # ValueError!
```

---

## Inheritance

### What is Inheritance? - The Family Tree Story 👨‍👩‍👧

Inheritance allows a class to get properties and methods from another class:

```
┌──────────────────────────────────────┐
│        ANIMAL (Parent Class)         │
│                                      │
│  Attributes:                         │
│  • name, age                         │
│                                      │
│  Methods:                            │
│  • eat(), sleep(), make_sound()      │
└──────────────────────────────────────┘
      ↑                    ↑           ↑
    inherits            inherits     inherits
      ↓                    ↓           ↓
┌─────────────┐    ┌─────────────┐  ┌─────────────┐
│   Dog       │    │   Cat       │  │   Bird      │
│(Child Class)│    │(Child Class)│  │(Child Class)│
│             │    │             │  │             │
│ ADD:        │    │ ADD:        │  │ ADD:        │
│ • fetch()   │    │ • scratch() │  │ • fly()     │
│ • bark()    │    │ • meow()    │  │ • sing()    │
└─────────────┘    └─────────────┘  └─────────────┘
```

### Simple Inheritance

```python
# Parent class
class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - inherits from Animal
class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def bark(self):
        return f"{self.name} says: Woof! Woof!"

# Create a dog
my_dog = Dog("Buddy", 3)

# Use inherited methods
print(my_dog.eat())    # Output: Buddy is eating (inherited)
print(my_dog.sleep())  # Output: Buddy is sleeping (inherited)

# Use dog-specific method
print(my_dog.bark())   # Output: Buddy says: Woof! Woof! (own)
```

### Overriding Methods

Child classes can replace parent methods:

```python
class Animal:
    """Base animal class"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    """Dog with own implementation"""
    
    def make_sound(self):
        """Override the parent method"""
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    """Cat with own implementation"""
    
    def make_sound(self):
        """Override the parent method"""
        return f"{self.name} meows: Meow!"

# Use different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.make_sound())  # Output: Buddy barks: Woof!
print(cat.make_sound())  # Output: Whiskers meows: Meow!
```

### Using super() - Call Parent Method

```python
class Vehicle:
    """Base vehicle class"""
    
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def describe(self):
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    """Car class that extends Vehicle"""
    
    def __init__(self, brand, year, doors=4):
        super().__init__(brand, year)  # Call parent's __init__
        self.doors = doors
    
    def describe(self):
        """Extend parent's describe method"""
        parent_desc = super().describe()  # Get parent's description
        return f"{parent_desc} with {self.doors} doors"

# Use the car
car = Car("Toyota", 2024, 4)
print(car.describe())  # Output: 2024 Toyota with 4 doors
```

---

## Polymorphism

### What is Polymorphism? - The Remote Control Story 📺

Polymorphism means "many forms". The same method name works differently for different objects:

```
┌──────────────────────────────────┐
│   REMOTE CONTROL (Same Button)   │
├──────────────────────────────────┤
│                                  │
│  When pressed on TV:             │
│  └→ TV turns on                  │
│                                  │
│  When pressed on Radio:          │
│  └→ Radio turns on               │
│                                  │
│  When pressed on Light:          │
│  └→ Light turns on               │
│                                  │
│  Same button → Different actions │
│                                  │
└──────────────────────────────────┘
```

### Polymorphism Example

```python
class Animal:
    """Base class"""
    
    def make_sound(self):
        pass

class Dog(Animal):
    """Dog implementation"""
    
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    """Cat implementation"""
    
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    """Cow implementation"""
    
    def make_sound(self):
        return "Moo!"

# The magic of polymorphism!
def animal_sound(animal):
    """Works with any animal"""
    print(animal.make_sound())

# Different animals, same function
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal_sound(animal)

# Output:
# Woof!
# Meow!
# Moo!
```

### Interface-like Polymorphism

```python
class Shape:
    """Base shape class"""
    
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    """Circle implementation"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    """Rectangle implementation"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    """Triangle implementation"""
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2

# Polymorphic function
def calculate_areas(shapes):
    """Works with any shape"""
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")

# Use with different shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

calculate_areas(shapes)
# Output:
# Area: 78.50
# Area: 24.00
# Area: 12.00
```

---

## Abstraction

### What is Abstraction? - The Car Dashboard Story 🚗

Abstraction hides complex details and shows only what's necessary:

```
┌──────────────────────────────┐
│   CAR DASHBOARD (Simple)     │
│                              │
│  ✓ Speed gauge              │
│  ✓ Fuel gauge               │
│  ✓ Temperature gauge         │
│                              │
│  (User doesn't see:)        │
│  ✗ Engine mechanics         │
│  ✗ Transmission details     │
│  ✗ Electrical systems       │
│                              │
│  Simple interface for       │
│  complex internal system!   │
│                              │
└──────────────────────────────┘
```

### Using Abstract Base Classes

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount):
        """Process payment - must be implemented by child classes"""
        pass
    
    @abstractmethod
    def refund(self, amount):
        """Process refund - must be implemented by child classes"""
        pass

class CreditCardProcessor(PaymentProcessor):
    """Concrete implementation for credit card"""
    
    def process_payment(self, amount):
        return f"Processing ${amount} via credit card"
    
    def refund(self, amount):
        return f"Refunding ${amount} to credit card"

class PayPalProcessor(PaymentProcessor):
    """Concrete implementation for PayPal"""
    
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"
    
    def refund(self, amount):
        return f"Refunding ${amount} to PayPal"

# Use the processors
cc = CreditCardProcessor()
paypal = PayPalProcessor()

print(cc.process_payment(100))      # Output: Processing $100 via credit card
print(paypal.process_payment(50))   # Output: Processing $50 via PayPal

# ❌ Cannot create abstract class directly:
# processor = PaymentProcessor()  # TypeError!
```

---

## Special Methods (Dunder Methods)

### Magic Methods - Making Objects Behave Like Built-ins ✨

Dunder methods (double underscore) let objects work with Python's built-in functions:

```python
class Book:
    """A book class with special methods"""
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """String representation (user-friendly)"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Developer representation"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """Length of book (number of pages)"""
        return self.pages
    
    def __eq__(self, other):
        """Check if two books are equal"""
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and 
                self.author == other.author)
    
    def __lt__(self, other):
        """Compare books by page count"""
        return self.pages < other.pages
    
    def __add__(self, other):
        """Add two books (combine total pages)"""
        return Book(
            f"{self.title} & {other.title}",
            f"{self.author} & {other.author}",
            self.pages + other.pages
        )

# Use the book
book1 = Book("Python 101", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)

print(str(book1))        # Output: 'Python 101' by John Doe
print(len(book1))        # Output: 300
print(book1 < book2)     # Output: True (300 < 450)
print(book1 == book2)    # Output: False

combined = book1 + book2
print(combined)          # Output: 'Python 101 & Advanced Python' by John Doe & Jane Smith
```

### Common Dunder Methods Reference

```python
class Product:
    """Product with various dunder methods"""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # String representations
    def __str__(self):          # print(), str()
        return f"{self.name}: ${self.price}"
    
    def __repr__(self):         # repr(), debugging
        return f"Product('{self.name}', {self.price})"
    
    # Comparisons
    def __eq__(self, other):    # ==
        return self.price == other.price
    
    def __lt__(self, other):    # <
        return self.price < other.price
    
    def __le__(self, other):    # <=
        return self.price <= other.price
    
    # Arithmetic
    def __add__(self, other):   # +
        return self.price + other.price
    
    def __sub__(self, other):   # -
        return self.price - other.price
    
    def __mul__(self, quantity):  # *
        return self.price * quantity
    
    # Size/Length
    def __len__(self):          # len()
        return int(self.price)
    
    # Callable
    def __call__(self):         # product()
        return f"Calling {self.name}"
    
    # Container operations
    def __contains__(self, item):  # in operator
        return item in self.name

# Use the product
p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 25)

print(str(p1))           # Output: Laptop: $1000
print(p1 > p2)           # Output: True
print(p1 + p2)           # Output: 1025
print(p1 * 2)            # Output: 2000
print(len(p1))           # Output: 1000
```

---

## Class vs Instance Variables

### The Difference - Shared vs Personal 🎯

Class variables are shared by all instances. Instance variables are unique to each object:

```
┌────────────────────────────────────────┐
│         CLASS vs INSTANCE VARIABLES    │
├────────────────────────────────────────┤
│                                        │
│  CLASS VARIABLE:                       │
│  ├─ defined in class body              │
│  ├─ shared by all instances            │
│  ├─ exists only once in memory         │
│  └─ accessed via class or instance     │
│                                        │
│  INSTANCE VARIABLE:                    │
│  ├─ defined in __init__                │
│  ├─ unique to each instance            │
│  ├─ each instance has its own copy     │
│  └─ accessed via instance only         │
│                                        │
└────────────────────────────────────────┘
```

### Example

```python
class Student:
    """Student class with class and instance variables"""
    
    school = "Python High School"  # Class variable (shared)
    student_count = 0              # Class variable (counter)
    
    def __init__(self, name, gpa):
        self.name = name           # Instance variable
        self.gpa = gpa             # Instance variable
        
        # Modify class variable
        Student.student_count += 1

# Create students
s1 = Student("Alice", 3.8)
s2 = Student("Bob", 3.5)
s3 = Student("Charlie", 3.9)

# Access instance variables
print(s1.name)           # Output: Alice
print(s2.name)           # Output: Bob

# Access class variables (shared)
print(s1.school)         # Output: Python High School
print(s2.school)         # Output: Python High School (same)
print(Student.student_count)  # Output: 3

# Change class variable
Student.school = "New Python Academy"
print(s1.school)         # Output: New Python Academy (changed for all)
print(s2.school)         # Output: New Python Academy (changed for all)
```

---

## Static and Class Methods

### Static Methods - No Access to Instance or Class 🔒

```python
class MathTools:
    """Class with static methods"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def is_even(n):
        """Check if number is even"""
        return n % 2 == 0

# Use without creating an instance
print(MathTools.add(5, 3))         # Output: 8
print(MathTools.multiply(4, 6))    # Output: 24
print(MathTools.is_even(10))       # Output: True

# Also works with instance
tools = MathTools()
print(tools.add(10, 20))           # Output: 30
```

### Class Methods - Access to Class Variables 🏛️

```python
class Counter:
    """Class with class methods"""
    
    count = 0
    
    def __init__(self, name):
        self.name = name
        Counter.count += 1
    
    @classmethod
    def get_total_count(cls):
        """Get total number of counters created"""
        return f"Total counters: {cls.count}"
    
    @classmethod
    def reset_count(cls):
        """Reset the counter"""
        cls.count = 0
        return "Count reset!"
    
    @classmethod
    def from_string(cls, data):
        """Create object from string"""
        name = data.split("-")[0]
        return cls(name)

# Create counters
c1 = Counter("Alice")
c2 = Counter("Bob")
c3 = Counter("Charlie")

print(Counter.get_total_count())  # Output: Total counters: 3

# Create from string
c4 = Counter.from_string("David-123")
print(Counter.get_total_count())  # Output: Total counters: 4

print(Counter.reset_count())      # Output: Count reset!
print(Counter.get_total_count())  # Output: Total counters: 0
```

---

## Properties and Decorators

### Using @property - Make Methods Look Like Attributes 🎁

```python
class Circle:
    """Circle with property decorators"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Get radius"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set radius with validation"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def diameter(self):
        """Get diameter (calculated)"""
        return self._radius * 2
    
    @property
    def area(self):
        """Get area (calculated)"""
        import math
        return math.pi * self._radius ** 2

# Use like attributes
circle = Circle(5)

print(circle.radius)      # Output: 5 (getter)
print(circle.diameter)    # Output: 10 (getter, calculated)
print(circle.area)        # Output: 78.53981633974483

circle.radius = 7         # Output: Uses setter
print(circle.diameter)    # Output: 14

# This will raise error
# circle.radius = -5      # ValueError!
```

---

## Composition

### Composition vs Inheritance - What to Choose? 🔄

Composition is "has-a" relationship. Inheritance is "is-a" relationship:

```
┌────────────────────────────────────────┐
│   INHERITANCE vs COMPOSITION           │
├────────────────────────────────────────┤
│                                        │
│  INHERITANCE (is-a):                   │
│  Dog IS-A Animal                       │
│  └─ Dog inherits from Animal           │
│                                        │
│  COMPOSITION (has-a):                  │
│  Car HAS-A Engine                      │
│  └─ Car contains an Engine             │
│                                        │
│  Rule: Prefer composition over         │
│        inheritance!                    │
│                                        │
└────────────────────────────────────────┘
```

### Composition Example

```python
class Engine:
    """Engine class"""
    
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine started with {self.horsepower} HP"

class Wheels:
    """Wheels class"""
    
    def __init__(self, size):
        self.size = size
    
    def roll(self):
        return f"Wheels ({self.size}in) are rolling"

class Car:
    """Car composed of Engine and Wheels"""
    
    def __init__(self, brand, hp, wheel_size):
        self.brand = brand
        self.engine = Engine(hp)        # Has-a Engine
        self.wheels = Wheels(wheel_size)  # Has-a Wheels
    
    def drive(self):
        """Drive the car using composed objects"""
        msg1 = self.engine.start()
        msg2 = self.wheels.roll()
        return f"{self.brand}: {msg1}, {msg2}"

# Use composition
car = Car("Toyota", 200, 18)
print(car.drive())
# Output: Toyota: Engine started with 200 HP, Wheels (18in) are rolling

# Access composed objects
print(car.engine.horsepower)  # Output: 200
print(car.wheels.size)        # Output: 18
```

---

## Advanced OOP Concepts

### Multiple Inheritance

```python
class Swimmer:
    """Can swim"""
    
    def swim(self):
        return "Swimming"

class Flyer:
    """Can fly"""
    
    def fly(self):
        return "Flying"

class Duck(Swimmer, Flyer):
    """Duck inherits from both"""
    
    def quack(self):
        return "Quack!"

# Duck can do everything
duck = Duck()
print(duck.swim())   # Output: Swimming
print(duck.fly())    # Output: Flying
print(duck.quack())  # Output: Quack!
```

### Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "From A"

class B(A):
    def method(self):
        return "From B"

class C(A):
    def method(self):
        return "From C"

class D(B, C):
    pass

# Check MRO
print(D.mro())  # Output: [D, B, C, A, object]

d = D()
print(d.method())  # Output: From B (follows MRO)
```

---

## Design Patterns

### Singleton Pattern - Only One Instance 🎯

```python
class Database:
    """Singleton database connection"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        self.connected = True
        return "Connected to database"
    
    def get_status(self):
        return "Connected" if self.connected else "Disconnected"

# Create instances
db1 = Database()
db2 = Database()

print(db1 is db2)       # Output: True (same object)

print(db1.connect())    # Output: Connected to database
print(db2.get_status()) # Output: Connected (same instance)
```

### Factory Pattern - Create Objects Dynamically 🏭

```python
class AnimalFactory:
    """Factory to create animals"""
    
    @staticmethod
    def create_animal(animal_type):
        """Create an animal based on type"""
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            return None

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Use factory
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```

---

## Practical Applications

### Application 1: Library Management System 📚

```python
from datetime import datetime, timedelta

class Book:
    """Represents a book"""
    
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    """Represents a library member"""
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Borrow a book"""
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            return f"{self.name} borrowed {book.title}"
        return f"{book.title} is not available"
    
    def return_book(self, book):
        """Return a book"""
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}"
        return f"{self.name} didn't borrow {book.title}"

class Library:
    """Represents a library"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        """Add a book to library"""
        self.books.append(book)
    
    def add_member(self, member):
        """Add a member to library"""
        self.members.append(member)
    
    def show_available_books(self):
        """Show all available books"""
        available = [b for b in self.books if b.available]
        return f"Available books: {[str(b) for b in available]}"

# Use the library
library = Library("City Library")

book1 = Book("Python 101", "John Doe", "ISBN001")
book2 = Book("Advanced Python", "Jane Smith", "ISBN002")

library.add_book(book1)
library.add_book(book2)

member = Member("Alice", "M001")
library.add_member(member)

print(member.borrow_book(book1))    # Output: Alice borrowed Python 101
print(library.show_available_books())  # Output: Available books: ['Advanced Python by Jane Smith']

print(member.return_book(book1))    # Output: Alice returned Python 101
print(library.show_available_books())  # Output: Available books: ['Python 101 by John Doe', 'Advanced Python by Jane Smith']
```

### Application 2: Game Characters System 🎮

```python
class Character:
    """Base character class"""
    
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = True
    
    def take_damage(self, amount):
        """Take damage"""
        self.health -= amount
        if self.health <= 0:
            self.is_alive = False
            return f"{self.name} is defeated!"
        return f"{self.name} took {amount} damage (Health: {self.health})"
    
    def attack(self, target):
        """Attack another character"""
        if not self.is_alive:
            return f"{self.name} is dead and can't attack!"
        return target.take_damage(self.damage)

class Warrior(Character):
    """Warrior character"""
    
    def __init__(self, name, health, damage, armor=10):
        super().__init__(name, health, damage)
        self.armor = armor
    
    def take_damage(self, amount):
        """Armor reduces damage"""
        reduced_damage = max(1, amount - self.armor)
        return super().take_damage(reduced_damage)
    
    def shield_bash(self, target):
        """Special attack"""
        return target.take_damage(self.damage * 2)

class Mage(Character):
    """Mage character"""
    
    def __init__(self, name, health, damage, mana=100):
        super().__init__(name, health, damage)
        self.mana = mana
    
    def fireball(self, target):
        """Special spell attack"""
        if self.mana >= 20:
            self.mana -= 20
            return target.take_damage(self.damage * 3)
        return "Not enough mana!"

# Create characters
warrior = Warrior("Conan", 100, 15, armor=10)
mage = Mage("Gandalf", 60, 10, mana=100)

# Battle
print(warrior.attack(mage))        # Warrior attacks
print(mage.fireball(warrior))      # Mage uses spell
print(warrior.shield_bash(mage))   # Warrior special attack
print(f"{mage.name} alive: {mage.is_alive}")  # Check status
```

### Application 3: Bank System 💳

```python
class BankAccount:
    """Base bank account"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transactions.append(("Deposit", amount, self._balance))
            return f"Deposited ${amount}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self.transactions.append(("Withdraw", amount, self._balance))
            return f"Withdrew ${amount}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return f"Balance: ${self._balance}"

class SavingsAccount(BankAccount):
    """Savings account with interest"""
    
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Interest applied: ${interest:.2f}"

class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""
    
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount > 0 and amount <= (self._balance + self.overdraft_limit):
            self._balance -= amount
            return f"Withdrew ${amount}"
        return "Exceeds overdraft limit"

# Use accounts
savings = SavingsAccount("Alice", 1000)
checking = CheckingAccount("Bob", 500)

print(savings.deposit(500))        # Output: Deposited $500
print(savings.apply_interest())    # Output: Interest applied: $75.00

print(checking.withdraw(600))      # Output: Withdrew $600 (overdraft)
print(checking.get_balance())      # Output: Balance: $-100
```

---

## Best Practices

### 1. Follow SOLID Principles 🏗️

```python
# S - Single Responsibility Principle
class User:
    """Handles user data only"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailService:
    """Handles email sending only"""
    def send_email(self, user, message):
        return f"Email sent to {user.email}: {message}"

# O - Open/Closed Principle
class Shape:
    """Open for extension, closed for modification"""
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
```

### 2. Use Type Hints 📝

```python
class Calculator:
    """Calculator with type hints"""
    
    def add(self, a: int, b: int) -> int:
        """Add two integers"""
        return a + b
    
    def divide(self, a: float, b: float) -> float:
        """Divide two floats"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Helps catch errors early
calc = Calculator()
print(calc.add(5, 3))        # Output: 8
# print(calc.add("5", 3))    # Type checking warns about this
```

### 3. Documentation with Docstrings 📚

```python
class Person:
    """
    Represents a person with name and age.
    
    Attributes:
        name (str): The person's name
        age (int): The person's age
    
    Methods:
        get_info(): Returns person information
        have_birthday(): Increases age by one
    """
    
    def __init__(self, name: str, age: int):
        """Initialize a person."""
        self.name = name
        self.age = age
    
    def get_info(self) -> str:
        """
        Get person information.
        
        Returns:
            str: A formatted string with person info
        """
        return f"{self.name} is {self.age} years old"
```

### 4. Keep Classes Focused ✨

```python
# ❌ Bad - Too many responsibilities
class User:
    def create_account(self):
        pass
    
    def send_email(self):
        pass
    
    def save_to_database(self):
        pass
    
    def process_payment(self):
        pass

# ✅ Good - Single responsibility
class User:
    """Represents user data"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailService:
    """Handles email operations"""
    def send_email(self, email, message):
        pass

class DatabaseService:
    """Handles database operations"""
    def save_user(self, user):
        pass

class PaymentService:
    """Handles payment operations"""
    def process_payment(self, user, amount):
        pass
```

### 5. Avoid Mutable Default Arguments ⚠️

```python
# ❌ Bad
class Container:
    def __init__(self, items=[]):
        self.items = items  # Shared across instances!

# ✅ Good
class Container:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

---

## Quick Reference Cheat Sheet 🎓

```
┌────────────────────────────────────────────────┐
│      OBJECT-ORIENTED PROGRAMMING SUMMARY       │
├────────────────────────────────────────────────┤
│                                                │
│  CLASS DEFINITION:                             │
│  class ClassName:                              │
│      def __init__(self, param):                │
│          self.attribute = param                │
│                                                │
│  CREATING OBJECTS:                             │
│  obj = ClassName(value)                        │
│                                                │
│  INHERITANCE:                                  │
│  class Child(Parent):                          │
│      def method(self):                         │
│          super().method()                      │
│                                                │
│  SPECIAL METHODS:                              │
│  __init__      - Constructor                   │
│  __str__       - String representation         │
│  __repr__      - Developer representation      │
│  __eq__        - Equality comparison           │
│  __lt__        - Less than comparison          │
│  __add__       - Addition operator             │
│                                                │
│  ENCAPSULATION:                                │
│  _private      - Protected (convention)        │
│  __private     - Name mangling                 │
│  @property     - Getter/Setter                 │
│                                                │
│  STATIC/CLASS METHODS:                         │
│  @staticmethod - No access to instance         │
│  @classmethod  - Access to class variables     │
│                                                │
└────────────────────────────────────────────────┘
```

---

## OOP Principles Summary 📋

```
┌────────────────────────────────────────────────┐
│    THE 4 PILLARS OF OOP                        │
├────────────────────────────────────────────────┤
│                                                │
│  1️⃣  ENCAPSULATION                             │
│      Hide internal details, expose interface   │
│      Keep data safe with getters/setters       │
│                                                │
│  2️⃣  INHERITANCE                               │
│      Child classes inherit from parents        │
│      Reuse code and extend functionality       │
│                                                │
│  3️⃣  POLYMORPHISM                              │
│      Same method name, different behavior      │
│      Objects respond to same interface         │
│                                                │
│  4️⃣  ABSTRACTION                               │
│      Hide complexity, show simplicity          │
│      Use abstract base classes                 │
│                                                │
└────────────────────────────────────────────────┘
```

---

## Practice Exercises

### Easy Level 🌟
1. Create a simple `Book` class with title and author
2. Create a `Car` class with brand and year attributes
3. Add methods to `Person` class (greet, eat, sleep)
4. Create a `Rectangle` class and calculate area

### Medium Level 🌟🌟
5. Create `Animal` parent class and `Dog`, `Cat` children
6. Implement dunder methods (__str__, __eq__, __add__)
7. Create class with static and class methods
8. Use @property decorator for getters/setters
9. Implement composition with multiple classes

### Hard Level 🌟🌟🌟
10. Create an abstract base class with multiple implementations
11. Implement multiple inheritance with proper MRO
12. Create a design pattern (Singleton, Factory, etc.)
13. Build a complete system (Library, Game, Bank)
14. Use all 4 OOP pillars in one project

---
