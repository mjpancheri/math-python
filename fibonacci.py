import time
import math


# use phi (golden ratio)
def fibonacci_binet(n):
    return int((((1 + 5**0.5) / 2) ** n - ((1 - 5**0.5) / 2) ** n) / 5**0.5)


def fibonacci_binet2(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi**n - (1 - phi) ** n) / math.sqrt(5))


def fibonacci_binet_lucas(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi) ** -n) / math.sqrt(5))


# use recursion
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# use memoization
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


start_time = time.time()

print(fibonacci_binet(1000))

print("--- {:.6f} seconds ---".format(time.time() - start_time))
