for x in "Python":
  print(x)

for y in ["a", "b", "c"]:
  print(y)

for j in range(5):
  print(j)

for x in range(0, 10, 2):
  print(x)

print(range(5))
print([1, 2, 3, 4, 5])

print(type(range(5)))

names = ["John", "Mary"]

# found = False
# for name in names:
#   if name.startswith("J"):
#     print("found")
#     found = True
#     break
# if not found:
#   print("Not Found")

found = False
for name in names:
  if name.startswith("J"):
    print("found")
    break
else:
  print("Not Found")