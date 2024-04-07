# Simple one line string
app_name = "This is string's in \"python\""
print(app_name)


# Multiline strings
description = '''
This is description of python program 
this comes in all new lines
Ends here
'''
print(description)


# Index of strings
print(app_name[0])
print(app_name[-1])

# Range of index
print(app_name[0:4])
print(app_name[:4])
print(app_name[1:-1])



# Formatted Strings
first = 'Kumar'
last = 'Mashalkar'
msg = f'{first} [{last}] is a coder'
print(msg)

# Calculate sring len function
print(len(description))

# String Operators / Methods
print(app_name.lower())
cap_app = app_name.upper()
print(cap_app)

# Find method
print(app_name.find('i'))
print(app_name.find('string'))
print('python' in app_name)

print(app_name.title())
# Find and Replace string
print(app_name.replace('python','advanced python'))

