print('Hello World')

# print('Hello World' -- SyntaxError: invalid syntax
# print('Hello World) -- SyntaxError: EOL while scanning string literal

name = input('What is your name?\n')
print('Hi, %s.' % name)

friends = ['Rohit', 'Mandira', 'Toan', 'Zach']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))
