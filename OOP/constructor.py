class Student:
    def _init_(self,x,y,z):
       self.name=x
       self.rollno=y
       self.marks=z

    def display(self):
        print("Student Name:{}\nRollno:{}\nMarks:{}",format(self.name,self.rollno,self.marks))

    s1=Student("siddhi",101,80)
    s1.display()
    s2=Student("sunny",102,90)
    s2.display()