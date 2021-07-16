"""Calculate value of pi to the digit num."""


from math import factorial
from decimal import Decimal, getcontext

getcontext().prec = 1000

pi_input = input('How many digits of pi would you like? ')
n = int(pi_input)


def cal(num):
    """Calculate value of pi to sigificant digit 'num'."""
    temp = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)

    for k in range(num):
        temp = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(temp) / Decimal(deno)

    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return round(pi, num)


print(cal(n))
