from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized


def factorial_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def fact(n: int, acc: int) -> int:
        if n <= 1:
            return acc
        return fact(n - 1, n * acc)

    def factorial(n: int) -> int:
        return fact(n, ___)

    return factorial
