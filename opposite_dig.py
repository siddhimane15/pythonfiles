for i in range(1,11):
    for j in range(1,11 ):
        if i==1 or i==10 or j==1 or j==10 or 11-i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  