def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    def has_divisor(d: int) -> bool:
        if d * d > n:
            return False
        if n % d == 0:
            return True
        return has_divisor(d + 2)

    return not has_divisor(3)
