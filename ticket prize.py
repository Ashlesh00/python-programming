age=int(input("enter the age of the person"))
if 0>=age>=3:
    print("ticket is free")
elif 4>=age>=12:
      print("ticket price is 10$")
elif 13>=age>=17:
      print("ticket price is 15$")
elif 18<=age: 
    print("ticket price is 20$")
else:
    print("invalid")
