course = "Python programming"
print(len(course))
# Print a charactor by index
print(course[0])
print(course[17])

# Print a charactor by index from last.
print(course[-1])
print(course[-18])

# Print a substring by start and last index
print(course[0:4])
print(course[:4])

# To print entire string
print(course)
print(course[0:])
print(course[:])

# The location
print(id(course))
print(id(course[3]))


message = 'python "programming'
print(message)

newWord =  "python \"programming \\"
print(newWord)

change = "python \"programming \n hello word"
print(change)

# Multi line
yellow = """
The color
is yellow
"""
print(yellow)

yellow = """The color
is yellow
"""

print(yellow)

# Formated strings
first = "John"
last = "cena"
full = first + " " + last # normal way
full = f"{first} {last} new"
full = f"{len(first)} {last}"
print(full)