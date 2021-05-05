from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n in (0, 1):
        return 1
    if n & 1:  # if n is odd, it's faster than checking with modulo
        return fib((n+1)//2 - 1) * (2*fib((n+1)//2) - fib((n+1)//2 - 1))
    a, b = fib(n//2 - 1), fib(n//2)
    return a**2 + b**2

inp = int(input("Which place of the fibonacci series do you want? "))
if inp > 3:
    print(fib(inp-2))
else:
    print(0 if inp == 1 else 1)
