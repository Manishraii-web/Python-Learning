# Factorial = classic recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Fibonacci = tree recursion
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# Binary Search = divide and conquer
def binary_search(arr, target, lo=0, hi=None):

    # first call setup
    if hi is None:
        hi = len(arr) - 1

    # base case
    if lo > hi:
        return -1

    mid = (lo + hi) // 2

    # target found
    if arr[mid] == target:
        return mid

    # search right half
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)

    # search left half
    else:
        return binary_search(arr, target, lo, mid - 1)


# Testing
print(factorial(6))

print([fib(i) for i in range(8)])

arr = [2, 5, 8, 12, 16, 24, 38, 56]

print(binary_search(arr, 24))