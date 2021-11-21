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

s1 = Student(2, 3, 5)
s2 = Student(12, 34, 22)

print(s1.avg())

# m1. m2, m3 are instance variables