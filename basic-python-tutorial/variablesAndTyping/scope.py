# Local  variable

# def greet():
#   if True:
#     message = "a"
#   print(message)

# greet()

# Global variable

message = "a"

def greet():
  global message
  message = "b"

greet()
print(message)