# Problem 5: give jumbled input but desired output :pass named arguments 
def print_kwargs(name,power):
    print("name:",name,"power:",power)
print_kwargs(power="lazer",name="superman")
# print_kwargs(power="lazer",name="superman",enemy="dr doom") but cand handel extra arguments
 

# kwargs:
def print_(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_(power="lazer",name="superman",enemy="dr doom")

