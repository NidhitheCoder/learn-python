class Computer:
  def __init__(self):
    self.name = "Judy"
    self.age = 22

  def update(self):
    self.age = 30

  def compare(self, other):
    if self.age == other.age:
      return True
    else:
      return False



c1 = Computer()
c2 = Computer()

# print(id(c1))
# print(id(c2))

c1.name ="Rishi"

print(c1.name)
print(c2.name)

print(c1.age)
c1.update()
print(c1.age)

if c1.compare(c2):
  print("They are equal")
else:
  print("They are different")