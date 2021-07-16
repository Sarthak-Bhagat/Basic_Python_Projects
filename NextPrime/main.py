"""Prim number checker."""


def is_prime(number):
    """Check if number is prime."""
    return all(number % i for i in range(2, number))


def next_prime(number):
    """Get the smallest next prime number."""
    return min([a for a in range(number+1, 2*number) if is_prime(a)])


inp = int(input("Enter a number "))
print(next_prime(inp))
