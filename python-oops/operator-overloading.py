a = 5
b = 'world'

# print(a + b) # Getting typeError unsupported operand

c = 5
d = 6

print(c + d)
print(int.__add__(c, d))

e = '5'
f = '7'
print(e + f)
print(str.__add__(e, f))