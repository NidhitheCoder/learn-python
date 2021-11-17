def multiply(*list):
  print(list)

multiply(2, 3, 4, 5)

def mutliply_items(*list):
  total = 1
  for number in list:
     total *= number
  return total

print(mutliply_items(1, 2, 3, 4, 5))



def save_user(**user):
  # print(user) # {'id': 1, 'name': 'admin'}
  print(user["name"]) # admin

save_user(id=1, name="admin")
