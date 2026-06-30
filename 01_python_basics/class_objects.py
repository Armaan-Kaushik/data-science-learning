



#Student Management System
class Student:
    def __init__(self, name, age, course, marks):
            self.name=name
            self.age=age
            self.course=course
            self.marks=marks

    def display_details(self):
        print("name    :",self.name  )
        print("age     :",self.age)
        print("course  :",self.course )
        print("marks   :",self.marks)

    def is_topper(self):
        if self.marks>=90:
            print(self.name," is a topper" )
        else:
            print(self.name, "is not a topper")

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.marks = new_marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks.")

s1=Student("Armaan",19,"Maths",93)
s1.display_details()
s1.is_topper()
s1.update_marks(98)
s2=Student("Sonia",19,"Finance",91)
s2.display_details()
s2.is_topper()
s3=Student("Yash",18,"English",28)
s3.display_details()
s3.is_topper()