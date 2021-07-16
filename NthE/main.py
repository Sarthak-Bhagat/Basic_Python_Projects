"""Caclulate power of e to the power n."""


import decimal


def factorial(number):
    """Get a list of factorials."""
    factorials = [1]
    for i in range(1, number + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials


def compute_e(number):
    """Get the value of E."""
    decimal.getcontext().prec = number + 1
    e = 2
    factorials = factorial(2 * number + 1)
    for i in range(1, number + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    return e


while True:
    num = int(input("What power of e do you want to compute? "))
    if 0 <= num <= 1000:
        break

print(str(compute_e(num))[:num + 1])
