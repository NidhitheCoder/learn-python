class Computer:
  def __init__(self):
    self.name = "Judy"
    self.age = 22

c1 = Computer()
c2 = Computer()

print(id(c1))
print(id(c2))