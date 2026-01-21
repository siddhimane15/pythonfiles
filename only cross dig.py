for i in range(1,11):
    for j in range(1,11 ):
        if  i==j or 11-i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 