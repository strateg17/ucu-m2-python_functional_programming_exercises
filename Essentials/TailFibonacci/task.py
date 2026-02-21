from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:

    @tail_call_optimized
    def fib_step(n: int, a: int, b: int) -> int:
        if n == 0:
            return a
        return fib_step(n - 1, b, a + b)

    def fibonacci(n: int) -> int:
        return fib_step(n, 0, 1)

    return fibonacci
