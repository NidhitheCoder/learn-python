# def greet():
#   if True:
#     message = "a"
#   print(message)

# greet()

message = "a"

def greet():
  global message
  message = "b"

greet()
print(message)