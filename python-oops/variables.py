class car:
  def __init__(self):
    self.mil = 10  # instance variable
    self.com = "BMW"  # instance variable

c1 = car()
c2 = car()

c1.mil =12

print(c1.com, c1.mil)
print(c2.com, c2.mil)