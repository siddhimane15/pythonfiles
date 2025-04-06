

class student:

    def __init__(self,height,degree):

        self.height = height
        self.degree = degree
        self.marks = 0
        self.subjects = ''

    def update_marks(self,value):

        self.marks += value
        return self.marks
    
    def update_subjects(self,sub):

        self.subjects += sub
        return self.subjects
    
    def details(self):

        print(f"Height: {self.height} Education: {self.degree} Marks: {self.marks} Subject: {self.subjects}")


student_1=student(5.3,'B.com')
student_1.update_marks(98)
student_1.update_subjects('english')
student_1.update_subjects('maths')
student_1.details()










