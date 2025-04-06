
def velocity(d,t):
    v=d/t
    return v

def momentum(mass,v):
    momentum=mass*v
    return momentum

def acc(dv,dt):
    acc=dv/dt
    return acc

def force(m,a):
    force=m*a
    return force

distance = 15 
time = 60
mass = 2000
dt = 10
dv = 15
ans = velocity(distance, time)
print(ans)

ans1=momentum(mass,ans)
print(ans1)

ans2=acc(dv,dt)
print(ans2)

ans3=force(mass,ans2)
print(ans3)



