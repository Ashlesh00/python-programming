amount=float(input("enter the amount in dollar"))
member=input("enter y for yes and n for no")
amount_n=amount-(0.1*amount)
if amount>=100 and member=='y':
    print(amount_n)
else:
    print(amount)
