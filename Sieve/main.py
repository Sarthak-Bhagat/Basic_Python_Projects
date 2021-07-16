"""Eratosthenes Sieve."""


from tqdm import tqdm


def basePrime(num):
    """Check if n is a multiple of any prime number."""
    for i in primes:
        if num % i == 0 and num != i:
            return False
    return True


def Prime(lst, num):
    """Create a list of prime numbers upto num."""
    return [i for i in lst if i % num != 0 or i == num]


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
L = int(100000)
sieve = [i for i in range(2, L) if basePrime(i)]
# print(sieve)

for i in tqdm(sieve):
    if i in primes:
        continue
    sieve = Prime(sieve, i)

print(sieve)
