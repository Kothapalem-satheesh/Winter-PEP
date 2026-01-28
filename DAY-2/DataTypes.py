"""Data types in Python are a way to classify data items. They represent the kind of value, which determines what operations can be performed on that data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes.

The following are standard or built-in data types in Python:

Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview"""


x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple



"""Numeric Data Types
Python numbers represent data that has a numeric value.
A numeric value can be an integer, a floating number or even a complex number."""


a=5
b=5.0
c=2+4j
print(type(a))
print(type(b))
print(type(c))


""" Sequence Data Types
A sequence is an ordered collection of items, which can be of similar or different data types. Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence data types of Python:

String Data Type
Python Strings are arrays of bytes representing Unicode characters. In Python, there is no character data type, a character is a string of length one. It is represented by str class.

Strings in Python can be created using single quotes, double quotes or even triple quotes. We can access individual characters of a String using index.

"""
s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

"""Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items. 
It is very flexible as items in a list do not need to be of the same type."""

# Lists in Python can be created by just placing sequence inside the square brackets[].

# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)



"""
Tuple Data Type
Tuple is an ordered collection of Python objects.
The only difference between a tuple and a list is that tuples are immutable.
Tuples cannot be modified after it is created.

Note: Tuples can also be created with a single element, 
but it is a bit tricky. 
Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple. 
"""

# initiate empty tuple
tup1 = ()

tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)


"""
Boolean Data Type
Python Boolean Data type is one of the two built-in values, 
True or False. Boolean objects that are equal to True are truthy (true) and those equal to False are falsy (false).
However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by class bool.
"""

print(type(True))
print(type(False))
# print(type(true))  

"""Traceback (most recent call last):
  File "/home/7e8862763fb66153d70824099d4f5fb7.py", line 8, in 
    print(type(true))
NameError: name 'true' is not defined"""



"""
Truthy and Falsy Values
In Python, truthy and falsy values are values that evaluate to True or False in a Boolean context.
Truthy values behave like True, while falsy values behave like False when used in conditions.
"""

if 1:
    print("1 is truthy")
if not 0:
    print("0 is falsy")
    
    


"""
Set Data Type
In Python Data Types, Set is an unordered collection of data types that is iterable,
mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
"""

# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)


"""
Dictionary Data Type
used to store data values like a map, unlike other Python Data Types,
a Dictionary holds a key: value pair. Key-value is provided in dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.
The dictionary can also be created by the built-in function dict().

Note  - Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 

"""
d={}
d={1:'geeks',2:'for',3:'geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)