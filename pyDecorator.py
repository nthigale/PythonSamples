def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


# function are First-Class objects, can be passed around as argument
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 5, 10)
result1 = calculate(subtract, 18, 6)
result2 = calculate(multiply, 7, 8)
print(result, result1, result2)


#Nested function
def outer_function():
    print("I am outer")

    def nested_function():
        print("I am inner")

    nested_function()

outer_function()


# Functions can be returned from other function
def main_func():
    print("**** I am main function ****")

    def nested_in_main_function():
        print("**** I am nested in main function ****")

    return nested_in_main_function


nested_in_main_function_call = main_func()
nested_in_main_function_call()


# Python decorator
## 1.  create a normal function, takes another function as an input
## 2. inside decorator function, nest wrapper function
## 3. execute the function passed in an argument
## 4. return wrapper function


def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function


import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello!")

def say_bye():
    print("Bye for now!")

say_hello()
say_bye()