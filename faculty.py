from user import User

class Faculty(User):
  """Class of faculty members"""

  def __init__(self, name, address, psu_id, office_address, office_phone):
    """Initializes the attributes of faculty from user then creates the new ones"""
    super().__init__(name, address, psu_id)
    self.office_address = office_address
    self.office_phone = office_phone

  def describe_user(self):
    """Describes the users attributes"""
    # Can return super().describe_user() + the new string
    print(f'The user name is {self.name}\nthe user address is {self.address}\nthe user PSU ID is {self.psu_id}\nthe user office address is {self.office_address}\nthe user office phone number is {self.office_phone} \n ')

  def __str__(self):
    return self.describe_user()

    


  

  