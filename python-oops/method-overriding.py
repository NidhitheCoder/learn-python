class A:

  def show(self):
    print('A in show')

class B(A):
  
  def show(self): # class B's show method override class A's show method.
    print('B in show')


a1 = B()
a1.show()
