
m1= int(input('enter marks obtained in sub1:'))
m2= int(input('enter marks obtained in sub2:'))
m3= int(input('enter marks obtained in sub3:'))
m4= int(input('enter marks obtained in sub4:'))
total_marks=m1+m2+m3+m4
avg_marks=float(total_marks/4)
print('total marks obtained:',total_marks)
print('aggreagate:',avg_marks)

if avg_marks>=75:
    print('distinction')
elif avg_marks>=60 and avg_marks<75:
    print('first class')
elif  avg_marks>=50 and avg_marks<60:
    print('second class') 

elif avg_marks>=40 and avg_marks<50:
    print('third class')

else :
    print('fail')  
   
#    
    
