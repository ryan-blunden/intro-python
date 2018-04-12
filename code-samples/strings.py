# Strings
name = 'ryan'
print(name.capitalize())

spaced_name = '  ryan  '
print('"{}"'.format(spaced_name.strip()))

names = 'BatMan,Robin,Wonder Woman,Hulk,Superman'
print(names.split(', '))  # Split by space by default

# String indexing the Python way
print(names.find('Robin'))
print(name[0:3])

# String formatting positional
first_name = 'Cat'
last_name = 'Woman'
email = 'cat_woman@villains.gotham.org'
print('{} {} is available at {}'.format(first_name, last_name, email))

# String formatting keys
print('{first_name} {last_name} is available at {contact}'.format(
    contact='cat_woman@villains.gotham.org',
    first_name='Cat',
    last_name='Woman'
))

# Formatting a list as a string
names_list = names.split(',')
name_str_list = ', '.join(names_list)
print('My fav super heroes are: {}'.format(name_str_list))

# Replacing text
users = ['jenny_mcbride', 'kevin_anderson', 'james_hopman']
print(users[0].replace('_', ' '))

# Replacing text, treating each item in the array like a line in a file where we want to replace every instance of a character in a file
users = [
    'jenny_mcbride',
    'kevin_anderson',
    'james_hopman'
]
print(
    ',\n'.join(users).replace('_', ' ')
)

# Usecase: We want to find james_hopman and replace with michael_jordan
users = [
    'jenny_mcbride',
    'kevin_anderson',
    'james_hopman'
]
print(','.join(users).replace('james_hopman', 'michael_jordan').split(','))
