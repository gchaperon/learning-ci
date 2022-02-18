import sys
import os


def nfibonacci(n: int) -> list[int]:
    print(os.name)
    """Returns the n first fib numbers, n=0 -> [], n=1 -> [0], n=2 -> [0, 1], ..."""
    s = [0, 1]
    for _ in range(2, n):
        s.append(s[-1] + s[-2])
    return s[:n]


def fibonacci(n: int) -> int:
    """Returns nth fib number, fib_0 = 0, fib_1 = 1, ..."""
    print(sys.platform)
    return nfibonacci(n + 1)[-1]
