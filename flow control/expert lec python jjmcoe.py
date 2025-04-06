data=input('please enter date and time in YYY-MM-DD HH:MI:SS.FF Format:')
newdata=data.split(' ')
date=newdata[0].split('-')
time=newdata[1].split(':')
print('date:',date[2],'month:',date[1],'year:',date[0],'hour:',time[0],'mins:',time[1],'sec:',time[2])



#vehicle problem