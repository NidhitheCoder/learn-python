class Computer:
  def config(self):
    print("i5, 16gb, 1TB")


comp1 = Computer()
Computer.config(comp1) # Call an object methods of a class

comp2 = Computer()
Computer.config(comp2)

# Call object itself to call the method
comp1.config()
comp2.config()

# print(type(comp1))

# a = '8'
# print(type(a))