import StudentClass as sc

"""
student_id = input("Student_ID: ")
student_name = input("Student Name: ")
student_dob = input("Student DOB: ")
student_classification = input("Classification (F,S,Jr,Sr): ")

person = S.Student('person', student_id, student_name, student_dob, student_classification)
"""
studentid = 1001
name = "John"
dob = "1-/11/2001"
classification = "junior"


student1 = sc.Student(studentid, name, dob, classification)

student1.calc_age()
student1.calc_register()


print(f"Student age is: {student1.get_age()}")
print(f"Student can register between: {student1.get_register()}")
