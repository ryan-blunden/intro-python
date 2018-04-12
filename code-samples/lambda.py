# Inline function.
# Executes a single statement and returns the result.


def square(x):
    return x * x


square(4)

square_lambda = lambda x: x * x  # noqa: E731
square_lambda(4)

multiply = lambda x, y: x * y  # noqa: E731
multiply(3, 4)

add_substract = lambda x, y: (x + y, x - y)  # noqa: E731
add_res, minus_res = add_substract(5, 3)
print(add_res, minus_res)
