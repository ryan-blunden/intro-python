# Inline function.
# Executes a single statement and returns the result.

def square(x):
    return x * x


square(4)

square_lambda = lambda x: x * x
square_lambda(4)

multiply = lambda x, y: x * y
multiply(3, 4)

add_substract = lambda x, y: (x + y, x - y)
add_res, minus_res = add_substract(5, 3)
print(add_res, minus_res)

## new courses?

# Introduction to programming with Python
# Python for programmers
# - What are the pre-requisites
