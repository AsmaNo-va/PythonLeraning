#VARIABLE=A container for a value(string,integer,float,boolean)
#        A variable behaves as if it was the value it contains
#string
first_name= "ASma"
food= "Briyani"
email="asma123@gmail.com"
print( first_name)
print(f"hello { first_name}")
print(f"I like {food}")
print(f"My mail is: {email}")
#integers
age =20
quantity=3
No_of_students=40
print(f"My age is:{age}")
print(f"I bought {quantity} items")
print(f"MY Class has {No_of_students} students")
#float
price =125.05
gpa=3.02
distance=4.5
print(f"price of briyani is: ${price}")
print(f"My GPA Is: {gpa}")
print(f"I Ran ABout: {distance} Km")
#boolean
is_student = False
for_sale = False
is_online= True
if is_online:
    print(" I am online")
else:
    print("Not Online")
if for_sale:
    print("That item is for sale")
else:
    print("Not for sale")

#print((f"Are you student?: {is_student}"))
#if is_student:
    #print("You are a student")
#else:
    #print(("you are not student"))