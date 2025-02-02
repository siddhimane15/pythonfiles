#List, dictionary, Tuples
#List is a organized collection of data which is further divided into twm types: Dictionary and Tuple
#Dictionary is a unorganized mutable list which has an assigned keyword for each element.
#Tuple is a nonmutable list or collection of data.

names = ['John','jennifer','alex','Jordan']
c=names[0]
print(c)
names.append('Johnathon')
#print(names)
names.remove('jennifer')
print(names)

numbers = ['1','2','3','4','5','6']
c=int(numbers[0])+int(numbers[5])
print(c)

#Dictionary 
student ={'name':'2','Roll Number':'071','Marks':'73'}
m=int(student['name'])*int(student['Marks'])
print(m)
student.update({'mobile no':'1234567890'})
print(student)
del student['Marks']
print(student)
student.pop('Roll Number')
print(student)

#tuple
nums= (1,2,3,5,4,6,7)
c=nums[0]*nums[6]
print(c)
