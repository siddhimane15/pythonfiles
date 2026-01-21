for i in range(1,12):
    for j in range(1,12 ):
        if  i==1 or i==11 or j==1 or j==11 or i>=j and 12-i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()