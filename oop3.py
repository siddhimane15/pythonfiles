
class mobile:
    def __init__ (self,brand,price):
        self.brand = brand
        self.price = price
        self.ram = None

    def iram(self,memory):
        self.ram = memory
        return self.ram


    def discount(self,value):
        self.price -= (self.price*value/100)
        return self.price
    
    def details(self):

        print(f"Brand: {self.brand} and price:{self.price} RAM: {self.ram}")
  
oppo_1 = mobile("oppo",20000)
oppo_1.discount(15)
oppo_1.iram('6GB')
oppo_1.details()

realme=mobile("realme",15000)
realme.discount(10)
realme.iram('4GB')
realme.details()



