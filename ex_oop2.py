

class vehicle:

    def __init__(self,brand):
        self.brand=brand

        self.speed = 0

    def increase(self,value):
        self.speed +=value

    def decrease(self,value):
        self.speed -=value

    def details(self):

        print(f"speed: {self.speed} and brand: {self.brand}")


car1=vehicle("Audi")
car1.increase(17)
car1.decrease(7)
car1.details()
fortuner=vehicle("fortuner")
fortuner.details()


#speed,brand,details