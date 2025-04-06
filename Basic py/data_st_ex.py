
data = [{'hello':1,'hi':3,'you':9},[29,12,3.5],[1,9],[3,8],{'name':21,'no':95},[6,90]]

def addition(x,y):

    ans = x+y
    #print(ans)

    return ans


x = data[0]['hello']
y = data[3][0]

print(addition(x,y))



def Sub(a,b):
    ans=a-b
    return ans

a=data[0]['you']
b=data[5][1]

print(Sub(a,b))