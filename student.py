from user import User

class Student(User):
  """Creates a subclass of users with students"""
  def __init__(self, name, address, psu_id, major, school_year, advisor):
    """Initializes the attributes for students"""
    super().__init__(name, address, psu_id)
    self.major = major
    self.school_year = school_year
    self.advisor = advisor



  def describe_user(self):
    """Describes the users attributes"""
    print(f'The user name is {self.name}\nthe user address is {self.address}\nthe user PSU ID is {self.psu_id}\nthe user major is {self.major}\nthe user school year is {self.school_year}\nthe user advisor is {self.advisor.describe_user()}\n')
diff --git a/faculty.py b/faculty.py
