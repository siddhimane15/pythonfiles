import math
from math import radians, sin, cos, sqrt, atan2
from rectangle import area_of_rectangle

'''def calculator(num1,num2):

    if operators=='+':
        ans=num1+num2
    
    elif operators=='-':
        ans=num1-num2
    elif operators=='*':
        ans=num1*num2

    elif operators=='/':
        ans=num1/num2

    elif operators=='%':
        ans=num1%num2 

    else:
       ans= print("Invalid Input...")

    return ans

x=float(input("Enter first number: "))
operators=input("Enter operators: ")
y=float(input("Enter second number: "))
z=calculator(x,y)
print(z)'''



def pythagoras(adj_side,front_side):
    h=(adj_side)**2 + (front_side)**2
    hp=math.sqrt(h)
    return hp

m=pythagoras(8,6)
print(m)


def area_of_triangle(adj_side,front_side):
    area=(1/2)*(adj_side)*(front_side)
    return area

m=area_of_triangle(12,13)
print(m)


def distance(lat1,lon1, lat2, lon2):
    #convert degrees to radians
    lat1,lon1, lat2,lon2 = map(radians,[lat1,lon1,lat2,lon2])

    #haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon2
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    earth_radius = 6371

    distance = earth_radius*c

    return distance 



latA, lonA = 17.0159955, 74.1161454
latB, lonB = 19.1335004, 72.9092555

distance = distance(latA, lonA, latB, lonB)
print(distance)


def add(a,b):
    add=(a)+(b)
    return add

m=add(35,56)
print(m)

#exceptions handling using ty-except

x=15
if x>10:
    try:
       y= "hello"+5
       print("Ok")

    except:
        print("Input Error")

else:
    print("No way..")

def subtraction():
    x=m-n 
    return x

m=15
n=8
y=subtraction()
print(y)

t=area_of_rectangle(4,5)
print(t)

def division():
    x=m/n
    return x

m=35
n=5
y=division()
print(y)
