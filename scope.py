user="Suryansh" # global
def name():
    # user="Soni"    #function 
    print(user)
name()

x=99
def  sum(y):
    z=x+y
    return z
print(sum(1))

# def fun():  #bad practice 
#     global x
#     x=12
# fun()
# print(x)

def f1():    #climbing  
    x=88
    def f2():
        print(x)
    f2()
f1()

def f1():    #climbing  
    x=88
    def f2():    # bag theroy ,closure
        print(x)
    return f2
myresult=f1()
myresult()






