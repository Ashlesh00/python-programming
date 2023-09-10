username=input("enter the username")
password=input("enetr the password")
if len(username)>=8 and len(password)>=5:
    print("username and password are valid") 
elif len(username)<5:
    print("username invalid")
elif len(password)<8:
    print("password invalid")

else:
    print("invalid username and password")
