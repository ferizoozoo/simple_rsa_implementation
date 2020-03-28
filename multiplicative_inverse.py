from check_prime import check_prime

def multiplicative_inverse_of_a_modulo_n(a, n):
    """
    Calculates the multiplicative inverse of a modulo n that satisfies the equation ns + at = 1 and
    returns the inverse t.

    Parameters
    ----------
    a : int
        The integer that is going to be inversed
    n : int
        The prime integer that a is going to divided by

    Returns
    -------
    int
        The remainder of the division of t by n, or the multiplicative inverse of a modulo n    

    """
    
    r, new_r = n, a
    t, new_t = 0, 1

    while new_r != 0:
        # q is the quotient
        q = r / new_r
        r, new_r = new_r, r - q * new_r
        t, new_t = new_t, t - q * new_t

    if r > 1:
        raise Exception('a is not invertible') 

    if t < 0:
        t += n   

    return t