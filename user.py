class User():
  """Declares the class of users"""
  
  def __init__(self, name, address, psu_id):
    """Initializes the attributes of name, address, psu_id"""
    self.name = name
    self.address = address
    self.psu_id = psu_id

  def describe_user(self):
    """Describes the users attributes"""
    print(f'The user name is {self.name}\nthe user address is {self.address}\nthe user PSU ID is {self.psu_id}\n')

  def __str__(self):
    """Outputs the description"""
    return self.describe_user()