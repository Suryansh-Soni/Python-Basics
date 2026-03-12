# # class:blueprint for creating objects
# # obj:real world entity from class
# class Student:
#     name="suryansh"  #attribute
# #creating object
# s1=Student()
# print(s1.name)  #accessing attribute

# class vechcle:
#     def __init__(self,name,color): #instance attribute ,
#         #  init constructor:run auto when the construtor is called 
#         self.name=name
#         self.color=color
# v1=vechcle("car","red")
# print(v1.name)
# print(v1.color)

# # methods: function inside class is called method
# class student :
#     def __init__(self,name,listOfmarks):
#         self.name=name
#         self.listOfmarks=listOfmarks
#     def avg(self):
#         sum=0
#         for i in self.listOfmarks:
#             sum=sum+i
#         return sum/len(self.listOfmarks)
# s1=student("suryansh",[90,80,70])
# print(s1.avg())

# by using @staticmethod 
# no need to write self all the time in methods
class student:
    def __init__(self, name, listOfmarks):
        self.name = name
        self.listOfmarks = listOfmarks

    @staticmethod
    def avg(listOfmarks):
        sum = 0
        for i in listOfmarks:
            sum = sum + i
        return sum / len(listOfmarks)

print(student.avg([90,80,70]))

# theroy of the 4 pillars of oops:
# 1.encapsulation:binding data and function together in a single unit is called encapsulation       
# 2.abstraction:hiding internal details and showing only functionality to the user is called abstraction
# 3.inheritance:acquiring properties and behaviors from parent class to child class is called
# 4.polymorphism:ability of an object to take many forms is called polymorphism


# basic class object
# class car:
#     brand ="Mahindra"
#     model="b6"
# my_car=car()
# print(my_car.brand)

class car:
    def __init__ (self,brand ,model):
        self.brand=brand
        self.model=model
    
my_car=car("suryansh","mahindra")
print(my_car.brand)



