
#write a python program to find roots of the given equation ax2+9bx+10
#take a=6, b=8
import math
a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))
r=b**2-4*a*c

if r>0:
    a1=((-b)+math.sqrt(r))/(2*a)
    a2=((-b)-math.sqrt(r))/(2*a)
    print(f"the roots of equation are: {a1},{a2}")

elif r==0:
    x2=(-b)/2*a
    print(f"the roots of equation are: {x2}")

else:
    print("no roots of this equation")        

