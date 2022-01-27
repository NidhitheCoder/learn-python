class Student:
  def __init__(self, m1, m2):
    self.m1 = m1
    self.m2 = m2

  def sum(self, a, b):
    s = a + b
    return s


s1 = Student(23, 34)

print(s1.sum(5, 8))
print(s1.sum(1, 2, 3)) # will return an error becouse of number of parameters