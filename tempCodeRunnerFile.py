class car:
    def __init__ (self,brand ,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand},{self.model}"
    
my_car=car("suryansh","mahindra")
print(my_car.brand)
print(my_car.full_name())