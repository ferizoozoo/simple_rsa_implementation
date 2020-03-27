from check_prime import check_prime
from random import getrandbits 

def prime_generator():
    """
    Generates a big prime integer.

    Returns
    -------
    int
        a prime number
    """

    k = 32

    prime = getrandbits(k)

    while not check_prime(prime):
        prime = getrandbits(k)

    return prime    