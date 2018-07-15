## 3. Base Cases ##

# Recursive factorial function
def factorial(n):
    # Check the base case
    
    # Recursive case
    return n * factorial(n - 1)
def factorial(n):
    # Check the base case
    if n == 0:
        return 1
    # Recursive case
    return n * factorial(n - 1)

factorial1 = factorial(1)
factorial5 = factorial(5)
factorial25 = factorial(25)

## 5. Fibonacci ##

# Add your function below
def fib(n):
    # Check the base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return fib(n - 1) + fib(n - 2)

fib1 = fib(1)
fib5 = fib(5)
fib25 = fib(25)