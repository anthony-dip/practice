from faculty import Faculty
from student import Student
from user import User

user_1 = User('Anthony', '173 nasejbf lane', 'amd7650')
user_1.describe_user()


user_faculty = Faculty("Julia Otulak", '13 hhre', 'jmo6372', '340 woodland', '216-637-8261')
user_faculty.describe_user()

student_1 = Student('Anthony', '173 nasejbf lane', 'amd7650', 'Computer science', 'Freshman', user_faculty )




