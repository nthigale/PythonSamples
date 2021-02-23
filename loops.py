# simple for loop with condition
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)


# inner functions
def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)


# function with default parameters
def foo(a, b=4, c=6):
    print(a, b, c)


foo(20, c=12)