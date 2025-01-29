
# eucleadean distance

def distance(p1, p2):

    distance = ((p2[0]-p1[0])**2 + (p2[1]-p1[1]**2))**1/2

    return distance

#coordinates

A = [0,0]
B = [4,0]
C= [1,4]
D= [3,3]

#coordinates of H1
H1_x = A[0]+C[0]/2
H1_y = A[1]+C[1]/2
print(H1_x,H1_y)

H1 = [H1_x,H1_y]

#coordinates of H2
H2_x =B[0]+D[0]/2
H2_y =B[1]+D[1]/2
print(H2_x,H2_y)

H2 = [H2_x,H2_y]

#distances

ab = distance(A,B)
bc =distance(B,C)
cd = -distance(C,D)
da =distance(A,D)
ac =distance(A,C)
dc =distance(D,C)
print(ab,bc,cd,da)

#height of triangle 1
bh1 = distance(B,H1)
bh2 = distance(B,H2)


#area of triangle 1
area1=1/2*ac*bh1
print(area1)

#area of triangle 2
area2=1/2*ac*bh2
print(area2)

#area of quadrilateral
c=area1+area2
print("Area of Quadrilateral: ",c)