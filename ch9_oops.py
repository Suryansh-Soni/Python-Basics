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
    totalcar=0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        car.totalcar+=1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand}, {self.__model}"
    def fule_type(self):
        return "petrol or diessel."
    
# staticmethod: no need of self
    @staticmethod
    def disc():
        return "cars are good."
    @property #to hide a property and restrics the visibility to limited .Cant override
    def model(self):
        return self.__model

my_car = car("suryansh", "mahindra")

# accessing through method

my_car.model="tesla"
print(my_car.get_brand())
print(my_car.full_name())


# Inheritance
class electricCar(car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


mycar2 = electricCar("Tesla", "Model S", "85KWH")
mycar3=electricCar("Tesla","b3","90kwh")

#encapsulation

print(mycar2.full_name())

# polymorphism
print(car.totalcar)
print(car.disc())

# making model readonly too.
my_car=car("tata","90")






