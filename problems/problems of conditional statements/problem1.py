# input and and define criteria and based on age and day there is discount

age=int(input("enter your age: "))
day="wednesady"

if(age<13):
    print("child")
elif(age<20):
    print("teenager")
elif(age<60):
    print("adult")
else:
    print("senior")


price=12 if age>=18 else 8
if day=="wednesady":
    price-=2
print(f"Today is {day},the ticket price is {price} ")
