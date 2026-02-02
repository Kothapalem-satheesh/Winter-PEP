# #code for the odd and even numbers

# n=int(input("enter a number: "))
# if n%2==0:
#     print("this is a even number")
# else:
#     print("the given number is odd number")
    
    
    
    
    
# #using ternary operator 
# a = 10
# b = 14
# c = 12

# res = a if (a >= b and a >= c) else (b if b >= c else c)
# print(res)




    
# import calendar 
# y = 2000
# if calendar.isleap(y):
#     print("Leap year")  
# else:
#     print("Not a leap year")



def is_leap(year):
    if (year%4==0 and year%100!=0)or(year%400==0):
        return True
    else:
        return False
    
year=int(input("enter a year"))
result=is_leap(year)
print(result)