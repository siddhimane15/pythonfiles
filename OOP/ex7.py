def distance(p1,p2):
    distance=((p2[0]-p1[0])**2+(p2[1]-p1[1]**2))**1/2
    return distance

A=[0,0]
B=[4,0]
C=[0,3]

m = [7,2,7]
n = [8,7,9]
mn = distance(m,n)
print(mn)

bc=distance(B,C)
ac=distance(A,C)
ab=distance(A,B)

print(bc,ac,ab)

area=1/2*ac*ab
print("area of triangle: ",area)