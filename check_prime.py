from gcd import gcd
from math import sqrt

def check_prime(a):
    """
    Checks if an integer is prime or not.

    Parameters
    ----------
    a : int 
        The integer to be checked

    Returns
    -------
    boolean
        returns the truth value of the number being prime or not    
    """

    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True        