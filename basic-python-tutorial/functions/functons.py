# def increament(number, by=1):
#   return (number, number + by)

def increament(number: int, by: int =1) -> tuple:
  return (number, number + by)


print(increament(2, by=3)) # this is called keyword argument
