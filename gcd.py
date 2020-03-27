def gcd(a, b):
    """
    Using the Euclidean algorithm for calculating the gcd of two integers a and b.

    Parameters
    ----------
    a : int 
        The first integer
    b : int 
        The second integer

    Returns
    -------
    int
        The GCD of two numbers    
    """

    # Base case
    if b == 0:
        return a

    # Recursive case    
    return gcd(b, a % b)    