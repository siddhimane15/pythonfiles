
import threading

def add(x,y):
    ans=x+y
    print(ans)
    return ans

#thread1=threading.Thread(target=add, args=(10,12,))
#thread1.start()

def sub(x,y):
    ans=x-y
    print(ans)
    return ans
#thread2=threading.Thread(target=sub,args=(15,18,))
#thread2.start()

def mul(x,y):
    ans=x*y
    print(ans)
    return ans
#thread3=threading.Thread(target=mul,args=(15,57,))
#thread3.start()

def div(x,y):
    ans=x/y
    print(ans)
    return ans
#thread4=threading.Thread(target=div,args=(15,5,))
#thread4.start()


def mod(x,y):
    ans=x%y
    print(ans)
    return ans
#thread5=threading.Thread(target=mod,args=(25,5,))
#thread5.start()


def word():
    for i in range(0,10):
        print("Hello")

#thread6=threading.Thread(target=word)
#thread6.start()



def word2():
    i=0
    while True:
        i+=1
        print(f"hello{i}")
        if i==10:
            break
#thread7=threading.Thread(target=word2)
#thread7.start()        

def table(x):

    for i in range(1,11):
        ans=x*i
        print(ans)

#thread=threading.Thread(target=table,args=(5,)) 
#thread.start()  

def table1(x):
    i=0
    while True:
        i+=1
        ans=x*i
        print(ans)
        if i==10:
            break
thread1=threading.Thread(target=table1,args=(10,))    
thread1.start()    






