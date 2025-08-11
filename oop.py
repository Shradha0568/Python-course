class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  
    def show_brand_model(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    

my_car =Car("Toyota", "Corolla")
name = my_car.show_brand_model()
print(name)  # Output: Brand: Toyota, Model: Corolla

