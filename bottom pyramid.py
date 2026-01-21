for i in range(1,12):
    for j in range(1,12 ):
        if  i==1 or i==11 or j==1 or j==11 or j<=i and 12-j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()