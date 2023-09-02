a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
s=(a+b+c)/2
out=(s*(s-a)*(s-b)*(s-c))**0.5
print(out)
