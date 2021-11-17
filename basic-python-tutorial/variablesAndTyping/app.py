student_count = 1000
rating = 4.999
is_published = False
course_name = "python"

# Mutliline string initialize  
description = """
mutliple
lines
"""

x = 1
y = 2

# Initialize mutliple variables in same line
a, b = 3, 4

# Assign same value for mutliple variables
x = y = 2

student = 5
print(type(student))

student = True
print(type(student))

apple: int = 10

print(id(apple))

apple = apple + 2
print(id(apple))

y = [1, 2, 3, 5]
print(id(y))

y.append(4)
print(id(y))