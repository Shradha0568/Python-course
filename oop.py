#there is no immediate garbage collection in python

class Car:
    def __init__(self, brand, model):
        self.__brand = brand # private attributes (can be accessed by same class but not in other classes)
        self.model = model  #public attributes 


    def get_brand(self):
        return self.__brand

    def show_brand_model(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    @staticmethod
    def static():
        print("this is staticmethod")




my_car =Car("Toyota", "Corolla")
Car.static()
#name = my_car.show_brand_model()
print(my_car.get_brand())  # Output: the name of the brand it is private variable



#inheritance :

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

tesle_car = ElectricCar("Tesla", "Model S", 100)
#print(tesle_car.show_brand_model())  # Output: Brand: Tesla, Model: Model S
print(f"Battery Size: {tesle_car.battery_size} kWh")  # Output: Battery Size: 100 kWh


#Encapsulation:


'''The variables that are written
 using _variableName are Protected and written __variableName are
private variables, these private variables can be accessed using getter and setters'''

#static method:

#it is the method which belongs to class instead of instance of class.

