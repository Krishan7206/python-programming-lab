username=input("enter the username")
password=input("enter the password")
if len(username)>=5 and len(password)>=8:
    print("valid username and password")
elif len(username)<5:
    print("invalid username")
elif len(password)<8:
    print("invalid password")
else:
    print("invald password and username")
