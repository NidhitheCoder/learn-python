def multiply(*list):
  print(list)

multiply(2, 3, 4, 5)

def mutliplyItems(*list):
  total = 1
  for number in list:
     total *= number
  return total

print(mutliplyItems(1, 2, 3, 4, 5))