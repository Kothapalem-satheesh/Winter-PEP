x = 5
name = "Satheesh"  
print(x)
print(name)


age = 21
_colour = "lilac"
total_score = 90

# invalid variables
# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen


#assigning the values to the variables 
x = 5
y = 3.14
z = "Hi"

# Dynamic Typing: Python variables are dynamically typed,
# meaning the same variable can hold different types of values during execution.

#multiple assignment
a=b=c=100
print(a,b,c)


x,y,z=1,2.5,"satheesh"
print(x,y,z)





#types of variables 
"""we can determine the type of a variable using the type()
function. This built-in function returns the type of the
object passed to it."""

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

# Deleting a Variable
"""We can remove a variable from the namespace using the del keyword. This deletes
the variable and frees up the memory it was using."""


x=10
del x
print(x)

"""
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 3, in <module>
NameError: name 'x' is not defined
"""


#practise
"""Swapping Two Variables: Using multiple assignments, 
we can swap the values of two variables without needing,
a temporary variable."""

a, b = 5, 10
a, b = b, a
print(a, b)


""" Counting Characters in a String: Assign the results
of multiple operations on a string to variables in one line"""

word ="python"
length=len(word)
print("length of the word:",length)

