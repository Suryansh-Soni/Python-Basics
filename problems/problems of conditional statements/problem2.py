# assign the grades according to marks scored 
marks=int(input("Enter your marks :"))
if marks>100:
    print("Enter valid marks.")
    exit()
if(marks>=90):
    grade ="A"
elif(marks>=80):
    grade="B"
elif(marks>=60):
    grade="C"
elif(marks>=40):
    grade="D"
else:
    grade="F"

print(f"According to your marks({marks}),your grade is {grade}")
