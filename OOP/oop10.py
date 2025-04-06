
from area_stc import triangle, square,circle

xyz = triangle(9,12)
print("area of triangle", xyz.area_of_triangle(),"m2")
print("perimeter of triangle",xyz.per_of_triangle(8,10),"m")

pqrs = square(8)
print("area of square ",pqrs.area_of_square(),"m2")
print("perimeter of square",pqrs.perimeter_of_square(),"m")

abc=circle(15)
print("area of circle",abc.area_of_circle(),"m2")
print("per of circle",abc.per_of_circle(),"m")
