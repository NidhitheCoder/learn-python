class A:
  def __init__(self):
    print('In A init')
    
  def feature1(self):
    print('Feature 1- A working')

  def feature2(self):
    print('Feature 2 working')

class B(A):

  def __init__(self):
    # Keyword SUPER helps to access all the methods of parent classes
    # If a class have multiple parent classes then SUPER keyword __init__ choose the left class based on Method resolution order(MRO). this is same for methods.
    # eg class C:(A, B); iSUPER of class C will take class A's init
    # You can use SUPER method inside all the methods, not event __init__ .
    super().__init__()
    print('In B init')
    
  def feature1(self):
    print('Feature 1-B is working')

  def feature4(self):
    print('Feture 4 is working')


a1 = B()
a1.feature1()