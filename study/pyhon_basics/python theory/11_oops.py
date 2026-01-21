# classes always naming convention e.g : class Car
# think of naming convension mainly
# in encapsulation we use getter and setter method to acces the attributes
# polymorphism it means that can do multiple different task   
# ###

class Car:
    total_car = 0

    def __init__(self , brand , model): # also called as constructor
        self.__brand = brand  #__ sets the attribut to private
        self.__model = model
        Car.total_car += 1

    def get_brand(self) :  #getter method 
        return self.__brand +" !"

    def full_name(self):  # it is an functionality 
        return f"{self.__brand} {self.__model}"
    # plymorphism
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod  ## To create an static method 
    def general_descr():
        return "Some description about cars"
    ## property Decorators to make an attribute read only 
    @property
    def model(self):
        return self.__model 


#Inheritance
class ElectricCar(Car):

    def __init__(self, __brand , __model , battery_size):
        super().__init__(__brand , __model)
        self.battery_size = battery_size
        def fuel_type(self):
            return "Electric Charge"
        

# my_car = ElectricCar("tesla","model_S","85kWh")

# print(my_car.get_brand())
# print(my_car.full_name())

# new_car1 = Car("BMW" , "S class" )
# print(new_car1.fuel_type())
## read setter 


## Class Variable
print(Car.total_car)

## static method
print(Car.general_descr())


##isinstance()
my_tesla = ElectricCar("tesla","model_S","85kWh")


print(isinstance(my_tesla,Car)) #true
print(isinstance(my_tesla, ElectricCar)) #true

#multiple inheritance 
class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine , Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())