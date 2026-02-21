from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    """
    Checks whether increment_fn behaves as a pure increment function.

    Purity criteria in this task:
      1) No mutation of the input object.
      2) Deterministic mapping: f(Integer(k)).value == k + 1
         for a wide range of k values.
    """
    # Test a broader range 
    for k in range(1, 101):
        inp = Integer(k)
        original_value = inp.value

        out = increment_fn(inp)

        # 1) Input must not be mutated
        if inp.value != original_value:
            return False

        # 2) Must return Integer
        if not isinstance(out, Integer):
            return False

        # 3) Must correctly increment
        if out.value != k + 1:
            return False

        # 4) Determinism check: calling again with same input value
        #    must produce same output value
        inp_again = Integer(k)
        out_again = increment_fn(inp_again)

        if out_again.value != k + 1:
            return False

    return True
