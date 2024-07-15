def fib(n):    # write Fibonacci series up to n
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b

def fib2(n):   # return Fibonacci series up to n
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

# Let's test the functions

# Test fib function
print("Fibonacci series up to 10:")
fib(10)

# Test fib2 function
print("\nFibonacci series up to 10 as a list:")
print(fib2(10))

# Test get_numeric function
print("\nNumber to word conversion:")
print(get_numeric(3))
print(get_numeric(5))

# Test my_function
print("\nTesting my_function with x = 2:")
my_function(2)

# Test my_function1
print("\nTesting my_function1 with x = 2 and a = 3:")
my_function1(2, 3)

# Test my_function2
print("\nTesting my_function2 with x = 2:")
my_function2(2)