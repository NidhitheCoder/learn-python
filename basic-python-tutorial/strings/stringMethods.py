course = "     Python programming"

print(course.upper())
print(course.lower())

# title() - capitalize a string/ first letter of every words in a string will be uppercase.
print(course.title())

# stripe() - remove unwanted spaces in left and right
# we can use lstrip() and rstrip() for get removed left side or right side of a string repectively.
print(course.strip())

# For find subtext
print(course.find('pro'))

# For replace string
print(course.replace("P", "_"))

# Replace string with anouther string.
print("programming" in course)
print("programming" not in course)