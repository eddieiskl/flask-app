def fib(n):  # write Fibonacci series up to n
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b


def fib2(n):  # return Fibonacci series up to n
    if n <= 0:
        return "Please enter a positive integer."
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


def get_numeric(number):
    numbers = ["zero", "one", "two", "three", "four"]
    if isinstance(number, int) and 0 <= number < len(numbers):
        return numbers[number]
    else:
        return "not supported"


a = 6


def my_function(x):
    print(x * a)


def my_function1(x, a):
    print(x * a)


def my_function2(x):
    a = 6
    print(x * a)