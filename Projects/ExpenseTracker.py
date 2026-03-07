# project details
# Add an expence with details like date,category,description,amount
# view all record expenses in a clean format
# calculate total spending so far
# exit program if user wnats 



expenses=[] #list of expenses
print("Welcome to Expense Tracker:Apna paisa sahi se istemal kre ")
while(True):
    print("----Menu----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenditure")
    print("4. Exit kra")

    choice=int(input("Please Enter Your Choice: "))

# Expense
    if(choice==1):
        date=input("Enter the date: ")
        category=input("Enter category (eg:Food,Fuel): ")
        description=input("Enter detail about your expenditure: ")
        amount=float(input("Enter the amount: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenses.append(expense)
        print("Expense added successfully.")
    elif(choice==2):
        if(len(expenses)==0):
            print("No expense added yet")
        else:
            print("---------- your Expenditure till now ---------- ")
            count=1
            for i in expenses:
                print(f'{count} ->{i["date"]},{i["category"]},{i["description"]},{i["amount"]}')
                count+=1
    elif(choice==3):
        total=0  
        for i in expenses:
            total+=i["amount"]  
        print("Total expenditure is:",total)     
    elif(choice==4):
        print("Thank you for using Expenditure App")
        break
    else:
        print("Invalid choice , select valid option")



