from check_prime import check_prime
from prime_generator import prime_generator
from gcd import gcd
from random import randint
from multiplicative_inverse import multiplicative_inverse_of_a_modulo_n

class RSA:
    """
    Simple implementation of the RSA algorithm.

    Attributes
    ----------
    p : int
        First prime integer
    q : int 
        Second prime integer
    n : int 
        Result of the multiplication of p and q
    totient : int 
        The totient of n ( or (p-1)*(q-1) )
    public_key : int 
        The generated public key
    private_key : int 
        The generated private key


    Methods
    --------
    public_key_generator() : int
        Populates the public_key variable.
    private_key_generator() : int
        Populates the private_key variable.
    """

    def __init__(self):
        """
        Generate two prime integers, p, q, multiply them, put the result
        in n, and calculate the totient by (p-1)*(q-1)

        """

        self.p = prime_generator()
        self.q = prime_generator()
        self.n = self.p * self.q
        self.totient = (self.p - 1) * (self.q - 1)

    def public_key_generator(self):
        """ Generate the public key. """
        e = randint(1, self.totient)
        while gcd(e, self.totient) != 1:
            e = randint(1, self.totient)

        self.public_key = (e, self.n)            

    def private_key_generator(self):
        """ Generate the private key. """
        self.private_key = multiplicative_inverse_of_a_modulo_n(self.public_key[0], self.totient)   