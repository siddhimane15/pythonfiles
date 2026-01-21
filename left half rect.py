for i in range(1,11):
    for j in range(1,11 ):
        if  i==1 or i==10 or j==1 or j==10 or j<=5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 