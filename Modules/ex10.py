
#!/usr/bin/python3
import math

a = float(input("Enter value of a: "))
b = float(input("enter value of b: "))
c = float(input("enter value of c: "))

r = b**2-4*a*c

if r>0:
    x1 = ((-b)+ math.sqrt(r))/(2*a)
    x2 = ((-b)- math.sqrt(r))/(2*a)
    print(f"The  roots of this equation are: {x1}, {x2}")


elif r==0:
    x = (-b)/2*a
    print(f"The  roots of this equation are: {x}")


else:
    print("no roots of this equation")