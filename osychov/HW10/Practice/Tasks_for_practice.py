class Car:
    def __init__(self, name ,kind , model):
        self.name = name
        self.kind  = kind
        self.model = model
        
    def start(self):
        return f"Car {self.name} {self.kind} {self.model} starts driving "
    
    def stop(self):
        return f"Car {self.name} {self.kind} {self.model} stops driving "
    
car1 = Car("porshe", "sport car", "999")
car2 = Car("mersedes", "sport car", "model")
print(car1.start())
print(car2.stop())
        