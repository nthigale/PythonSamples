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

## for loop
for _ in range(10):
   print ('_ in for loop range to iterate ')


## While loop to print all odd numbers in 1 to 100
n=1
print ('print even numbers 1-100')
while n < 100:
    if n % 2 == 0:
        n += 1
        continue
    else:
        n += 1
    print(n)

scores = [34, 67, 99, 105, 86]
for s in scores:
    if s > 100:
        print("Invalid")
        break
    print (f'from break loop {s}')
print(s)