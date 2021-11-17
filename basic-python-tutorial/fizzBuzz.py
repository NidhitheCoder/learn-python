def fizz_buzz(input):
  fizz = input % 3 == 0
  buzz = input % 5 == 0
  fizzBuzz = fizz and buzz

  if fizzBuzz:
    return "FizzBuzz"
  elif fizz:
    return "Fizz"
  elif buzz:
    return "Buzz"
  else:
    return input

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(22))
print(fizz_buzz(30))
print(fizz_buzz(7))
print(fizz_buzz(33))
print(fizz_buzz(45))