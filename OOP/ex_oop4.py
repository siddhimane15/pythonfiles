
class personal_information:

    def __init__(self, name, mob, address,email):

        self.name = name
        self.mob = mob
        self.address = address
        self.email = email

    def output(self):
        print(f"Name:{self.name}\nmob: {self.mob}\naddress: {self.address}\nEmail:{self.email}")

class Additional_Information(personal_information):
    def __init__(self,name,mob,address,email,eddu,roll):
        
        super().__init__(name,mob,address,email)

        self.eddu=eddu
        self.roll=roll

    def information(self):
        print(f"Name:{self.name}\nmob: {self.mob}\naddress: {self.address}\nEmail:{self.email}\nEducation: {self.eddu}\nRoll No.: {self.roll}")

shanakar_mane = personal_information('shankar','1234567890', 'assssscz','xdrxc ')
shanakar_mane.output()


siddhi=Additional_Information('siddhi','1234567896','abhgbhcbsa','dczsg','dczscz','25')
#siddhi.output()
siddhi.information()




        

    





