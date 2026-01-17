# classes always naming convention e.g : class Car
# think of naming convension mainly 
# ###

class Car:
    def __init__(self , brand , model): # also called as constructor
        self.__brand = brand  #__ sets the attribut to private
        self.model = model

    def get_brand(self) :  #getter method 
        return self.brand +" !"

    def full_name(self):  # it is an functionality 
        return f"{self.brand} {self.model}"


#Inheritance
class ElectricCar(Car):
    def __init__(self, brand , model , battery_size):
        super().__init__(   brand , model)
        self.battery_size = battery_size
my_car = ElectricCar("tesla","model_S","85kWh")
print(my_car.brand)
print(my_car.get_brand())
print(my_car.full_name())