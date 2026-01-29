


age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
    
    
    
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


#shorthand if else

marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"Result: {res}")




#ternary operator
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


age=20
s= "adult" if age >=18 else  "Minor"
print(s)


#match case statements
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")


