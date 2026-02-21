from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def fibonacci(n: int) -> int:
        if n < 0:
            raise ValueError('fibonacci is undefined for negative numbers')
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci
