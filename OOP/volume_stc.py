
class cube:

    def __init__(self,side):
        self.side = side

    def vol_of_cube(self):

        volume = (self.side)**3
        return  volume

class pyramid:

    def __init__(self,base,height):
        self.base=base
        self.height=height

    def vol_of_pyramid(self):

        volume=((1/3)*self.base*self.height)  
        return volume
    
class sphere:
    def __init__(self,pi,radius) :
        self.pi=pi
        self.radius=radius

    def vol_of_sphere(self):
        volume=((4/3)*self.pi*self.radius**3) 
        return volume
    
class cylinder:
    def __init__(self,pi,radius,height):
        self.pi=pi
        self.radius=radius
        self.height=height

    def vol_of_cylinder(self):
        volume=self.pi*self.radius**2*self.height
        return volume    
        

      
    




      