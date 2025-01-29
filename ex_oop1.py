
class vehicle:

    def __init__(self,brand,engine,size):
        self.brand = brand
        self.engine = engine
        self.size = size
        self.speed = 0
        self.price = 2500000

    def accelerate(self,increment):

        self.speed += increment

    def decelerate(self,decrement):

        self.speed -= decrement

    def value(self, year):

        self.price -= year

    def display(self):

        print(f"The speed of the vehicle brand is: {self.brand} with engine: {self.engine} and price:{self.price} and size: {self.size} has speed of {self.speed} mph")

#create the instances of the vehicle object
        
car1=vehicle("Audi","audi500cc","15x5")
car1.display()
