class Employee:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.fullname = firstname + " " + lastname
    self.email = firstname.lower() + "." + lastname.lower() + "@company.com"


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")

print(emp_1.fullname)
print(emp_2.email)