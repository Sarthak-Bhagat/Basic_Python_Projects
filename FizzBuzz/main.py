"""Fizzbuzz."""


def fizz(num):
    """Check if n is a multiple of 3 or 5 or neither."""
    return ((num % 3 == 0)*"Fizz" + (num % 5 == 0)*"Buzz") or num


def buzz():
    """Convert output from fizz into a printable format."""
    return "\n".join([str(fizz(i)) for i in range(100001)])


if __name__ == "__main__":
    print(buzz())
