class A:
  def __init__(self):
    print('In A init')
    
  def feature1(self):
    print('Feature 1 working')

  def feature2(self):
    print('Feature 2 working')

class B(A):
  def feature3(self):
    print('Feature 3 is working')

  def feature4(self):
    print('Feture 4 is working')


a1 = A()