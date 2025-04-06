

#A plane has takeoff speed of 88.30m/s and requires 1365m to reach that speed. 
#Determine the acceleration of the plane and time required to reach this speed.

class plane:

    def __init__(self,takeoff_speed, distance):

        self.takeoff_speed=takeoff_speed
        self.distance=distance

    def accel(self):

        acceleration=(self.takeoff_speed**2)/(2*self.distance)

        return acceleration
    
    def time(self):

        acceleration = self.accel()

        t = (self.takeoff_speed)/acceleration
        return t
    
fortuner=plane(88.30,1365)
acceleration=fortuner.accel()
time=fortuner.time()

print(f"acceleration of the plane:{acceleration}m/s2 and time :{time}sec")

        