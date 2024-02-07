class Vehicle:
    def __init__(self,type):
        self.type=type
class Automobile(Vehicle):
    def __init__(self, vehicle_type):
        super().__init__(vehicle_type)
        self.year=""
        self.make=""
        self.model=""
        self.doors=""
        self.roof=""
    def get_input(self):
        self.year=input("what year is it: ")
        self.make=input("what make is it: ")
        self.model=input("what model is it: ")
        self.doors=input("how many doors: ")
        self.roof=input("what roof type: ")
    def display(self):
         print("Vehicle type: ",self.type)
         print("year: ",self.year)
         print("make: ",self.make)
         print("model: ",self.model)
         print("doors: ",self.doors)
         print("roof: ",self.roof)
car=Vehicle(input("what is your vehicle type: "))
Vehicle1 = Automobile(car.type)
Vehicle1.get_input()
print()
Vehicle1.display()