# Create a Car class with the attributes name, kind, model
# and methods of start and stop, which indicate information
# that the car started or stopped accordingly.

class Car:
    car_count = 1

    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model
        self.count = self.car_count
        self.__class__.car_count += 1

    def get_start(self):
        print(f"The car №{self.count} {self.name} {self.model} has started!")

    def get_stop(self):
        print(f"The car №{self.count} {self.name} {self.model} has stopped!")

    def __str__(self):
        return f"Car №{self.count}: name {self.name}; " \
               f"kind {self.kind}; model {self.model}."


car_1 = Car("Porsche", "Sports Car", "911 GT3 RS")
car_2 = Car("Mercedes-Benz", "Supercar", "McLaren 722")
car_3 = Car("Bugatti", "Hypercar", "Bugatti Veyron")
print(f"The number of created objects of the 'Car' class: {Car.car_count - 1}")
car_1.get_start()
car_2.get_stop()
print(car_3)
