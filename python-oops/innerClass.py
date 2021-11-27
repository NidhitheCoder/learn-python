class Student:  # Outer class
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno
    self.lap = self.Laptop()

  def show(self):
    print(self.name, self.rollno)
    self.lap.show() 

  class Laptop:    # Inner class
    def __init__(self):
      self.brand = 'HP'
      self.cpu = 'i5'
      self.ram = 8

    def show(self):
      print(self.brand, self.brand, self.cpu)

s1 = Student('Naveen', 1)
s2 = Student('Liya', 2)

# print(s1.name, s1.rollno)

s1.show()

# create an object for innerclass laptop inside outer class
# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))

# create an object for laptop outside of the outer class
lap1 = Student.Laptop()