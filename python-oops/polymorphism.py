# x = 5

# x = 'Smith'

# class PyCharm:
#   def execute(self):
#     print('Compailing')
#     print('Running')

# class MyEditor:
#     def execute(self):
#       print('Spell check')
#       print('Convention check')
#       print('Compailing')
#       print('Running')

# class Laptop:

#   def code(self, ide):
#     ide.execute()

# # ide = PyCharm()
# ide = MyEditor()

# lap1 = Laptop()
# lap1.code(ide)




#  # Oeprator overloading

class Student:
  def __init__(self, m1, m2):
    self.m1 = m1
    self.m2 = m2

  def __add__(self, other):
    m1 = self.m1 + other.m1
    m2 = self.m2 + other.m2
    s3 = Student(m1, m2)

    return s3

  def __gt__(self, other):
    r1 = self.m1 + self.m2
    r2 = other.m1 + other.m2
    
    if r1 > r2:
      return True
    return False
  
  def __str__(self):
    # return self.m1, self.m2
    return ' {} {}'.format(self.m1, self.m2)

s1 = Student(58, 68)
s2 = Student(495, 34)

s3 = s1 + s2  # -> Student.__add__(s1, s2)

print(s3.m1) # 103
print(s3.m2) # 102

if ( s1 > s2):
  print('s1 wins')
else:
  print('s2 wins')

a = 9
print(a) # print value of 'a'. if we print a then we call a.__str__()
print(a.__str__())

print(s1.__str__())  # Print address of 's1'
print(s1)

print(s2)