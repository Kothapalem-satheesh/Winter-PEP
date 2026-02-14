# A dictionary stores data in key-value pairs. Like a real dictionary 
# you look up a word (key) to get its definition (value).

# student = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A",
#     "gpa": 3.8
# }

# print(type(student))  # Output: <class 'dict'>




# student = {"name": "Alice", "age": 20, "grade": "A"}
# # Access by key
# print(student["name"])      # Output: "Alice"
# print(student["age"])       # Output: 20

# # Safe access with get()
# print(student.get("name"))  # Output: "Alice"
# print(student.get("city"))  # Output: None (key doesn't exist)
# print(student.get("city", "Unknown"))  # Output: "Unknown" (default value)





# student = {"name": "Alice", "age": 20}
# # Adding/updating items
# student["grade"] = "A"      # Add new key-value pair
# student["age"] = 21         # Update existing value

# print(student)  # Output: {'name': 'Alice', 'age': 21, 'grade': 'A'}

# # Removing items
# del student["grade"]        # Delete a key-value pair
# student.pop("age")          # Remove and return value
# student.clear()             # Remove all items

# # Dictionary methods
# student = {"name": "Alice", "age": 20, "grade": "A"}

# keys = student.keys()           # Get all keys
# values = student.values()       # Get all values
# items = student.items()         # Get key-value pairs

# print(list(keys))    # Output: ['name', 'age', 'grade']
# print(list(values))  # Output: ['Alice', 20, 'A']
# print(list(items))   # Output: [('name', 'Alice'), ('age', 20), ('grade', 'A')]

# # Check existence
# print("name" in student)    # Output: True
# print("city" in student)    # Output: False



# # Dictionary Comprehension
# # Create a dictionary of squares
# squares_dict = {x: x**2 for x in range(1, 6)}
# print(squares_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# # With conditions
# even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# print(even_squares)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}



# # Iterating Through Dictionaries
# student = {"name": "Alice", "age": 20, "grade": "A"}

# # Iterate over keys
# for key in student:
#     print(key)  # Output: name, age, grade

# # Iterate over values
# for value in student.values():
#     print(value)  # Output: Alice, 20, A

# # Iterate over key-value pairs
# for key, value in student.items():
#     print(f"{key}: {value}")
#     # Output: name: Alice
#     #         age: 20
#     #         grade: A
    
    
    
    
# my_dict={'name':'Alice','age':35,'city':'new York'}
# print(f"original dictionary:{my_dict}")


# #adding new key-value pair
# my_dict['profession']='Doctor'
# print(f"updated dictonary after adding 'profession':{my_dict}")


# my_dict['age']=50
# print(f"updated  age {my_dict}")

# print('city:',my_dict['city'])


# my_dict={'name':'Alice','age':35,'city':'new yort','profession':'Doctor'}
# print(f"original dictionary: {my_dict}")

# del my_dict['profession']
# print(f"updated dictonary after removing 'profession':{my_dict}")



my_dict={'name':'Alice','age':35,'city':'new York'}
my_dict['profession']='engineer'
print(my_dict)

print("printing all key-value pairs: ")  
for name,value in my_dict.items():
    print(f"{name} :{value}")
    
def check_key_exists(dictionary,key_to_check):
    return key_to_check in dictionary
key1='age'
print(f"Does '{key1}'exist? {check_key_exists(my_dict,key1)}")




#excercise3
# convert two python lists into a dictionary

keys=['Ten','Twenty','thirty']
values=[10,20,30]

res_dict=dict(zip(keys,values))
print(res_dict)

#using a loop and update() method 

keys=['Ten','Twenty','Thirty']
values=[10,20,30]



res_dict=dict()
for i in range(len(keys)):
    res_dict.update({keys[i]:values[i]})
print(res_dict)



my_dict={'name':'satheesh','age':35,'city':'new York'}
print(f"dictonary:{my_dict}")


my_dict.clear()
print(f"dictonary after removing all the items: {my_dict}")



# merge two python dictionaries into one
dict1={'name':'satheesh','age':18,'city':'india'}
dict2={'name':'kothapalem satheesh','age':19,'city':'india'}


dict3={**dict1,**dict2}
print(dict3)

#  Rule:

# If the same key exists in both dictionaries, the value from the LAST dictionary wins.

# Here duplicate keys are:

# 'name'

# 'age'

# 'city'

# So Python does this:

# First adds from dict1:

# {'name':'satheesh', 'age':18, 'city':'india'}
# Then adds from dict2 → overwrites same keys:

# name → becomes 'kothapalem satheesh'

# age → becomes 19

# city → remains 'india'
#order matters 


#count character frequencies



def count_char_frequencies(input_string):
    frequency_dict={}
    for char in input_string:
        frequency_dict[char]=frequency_dict.get(char,0)+1
    return frequency_dict

string1='jessa'
print(f"frequencies for '{string1}':{count_char_frequencies(string1)}")






