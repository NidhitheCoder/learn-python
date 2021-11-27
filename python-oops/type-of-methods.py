class Student:
  school = "Kim jim"
  def __init__(self, m1, m2, m3):
    self.m1 = m1
    self.m2 = m2
    self.m3 = m3
  
  def avg(self):
    return self.m1 + self.m2 + self.m3 / 3

  def get_m1(self): 
    return self.m1

  def set_m1(self, value):
    self.m1 = value

  @classmethod    # decodeters
  def getSchool(cls):
    return cls.school

  def info():
    print('This is student')


s1 = Student(2, 3, 5)
s2 = Student(12, 34, 22)

print(s1.m1) # get value of m1 using variables.
print(s1.get_m1()) # get value of m1 using methods.

# Calling instance methods
print(s1.avg())

# m1. m2, m3 are instance variables

# Calling class methods
print(Student.getSchool())

# calling static methods
Student.info()