
            
# class person:
#     def __init__(self,name,country):
#         self.name=name
#         self.country=country #class variable 
#     def greeting(self):
#         if self.country=='india':
#             print(f"namasthe{self.country}")
#         else:
#             print(f"hello{self.name}")
            
# p=person("satheesh","india")
# p.greeting()


# print(p.name)


# #attribut creating the outside of the class
# p.gender="male"
# print(p.gender)



# p.age=23
# print(p.age)



# #reference variable
# class person:
#     def __init__(self):
#         self.name="satheesh"
#         self.country="india"
        
# result=person()
# print(result)
# print(id(result))
# q=result
# print(id(q))

# print(p.name)
# print(q.name)



# # pass by reference in opp
# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# def greeting(person):
#     print(f"hii my name is {person.name} and my gender is {person.gender}")
#     p1=Person("alex","male")
#     return p1

# result = Person("kothapalem satheesh", "male")

# a=greeting(result)
# print(a.name)
# print(a.gender)

# mutability in the objects
# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# #outside of class
# def greeting(person):
#     person.name="Alex"
#     return person
    
# p=Person("satheesh","Male")
# print(id(p))

# a=greeting(p)
# print(a.name)
# print(a.gender)

# print(id(a))
# print(id(p))





# class Person:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country

#     def __str__(self):
#         return f"Name: {self.name}, Country: {self.country}"

# p1 = Person("satheesh", "india")
# print(p1)


# #what is instance variable in oop
# class Person:
#     def __init__(self,name,country):#parameters
#         self.name=name
#         self.country=country 
# p1=Person("satheesh","india")     
# p2=Person("mouni","germany")
# p3=Person("ammulu","uk")


# print(id(p1))
# print(id(p2))
# print(id(p3))

# print(p2.name)
# print(p3.name)
#we cant store diffent different names and you cant use it use oop 

#encapsulation 



