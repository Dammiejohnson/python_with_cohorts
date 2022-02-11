# class Student_10:
#     # student_name = "student name"
#     # marks = 0
#     def __init__(self):
#         self.student_name = "student_name"
#         self.marks = 0

#     def set_student_name(self, student_name):
#         self.student_name = student_name
#     def set_marks(self, marks):
#         self.marks = marks

# # student = Student_10()
# student = Student_10()
# print("Original values are: ")
# print(student.student_name)
# print(student.marks)

# print("Modified values are: ")
# student.set_student_name("Sanni Oluwadamilola")
# print(student.student_name)

# student.set_marks(45)
# print(student.marks)


class Student_10:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    

student = Student_10("scv119", "dami")
# to add an attribute to the class
student.__setattr__("student_class", "ss3")
setattr(student, "student_class", "sss3")
# to remove an attribut
delattr(student, "student_name")
# student.__delattr__("student_name")

# to print out in a dictionary forms
print(student.__dict__) 
# to print out in the order of parameter in thr initialiser
# print(student.student_id,student.student_name, student.student_class)

# to add an attribute to the dict of the class like an update format
# student.update({"location": "Abuja"}) 
# print(student.__dict__)


