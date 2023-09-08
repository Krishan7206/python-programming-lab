age=float(input("enter the age of person"))
if 0>=age>=3:
    print("ticket is free")
elif 4>=age>=12:
    print("ticket price=$10")
elif 13>=age>=17:
    print("ticket price=$15")
elif 18<=age:
    print("ticket price=$20")
else:
    print("age is invalid") 
