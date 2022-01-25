x = 5

x = 'Smith'

class PyCharm:
  def execute(self):
    print('Compailing')
    print('Running')

class MyEditor:
    def execute(self):
      print('Spell check')
      print('Convention check')
      print('Compailing')
      print('Running')

class Laptop:

  def code(self, ide):
    ide.execute()

# ide = PyCharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)