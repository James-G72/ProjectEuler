def prime_factors(integer):
    """
    Returns the full list of the prime factors for the given integer.
    :param integer:
    :return:
    """
    assert isinstance(integer, int), f"Can only return prime factors of an integer not {type(integer)}."
    i = 2
    factors = []
    while i * i <= integer:
        if integer % i:
            i += 1
        else:
            integer //= i
            factors.append(i)
    if integer > 1:
        factors.append(integer)
    return factors


def all_factors(num):
    """
    Brute for finding all factors
    :param num: number to find factors of
    :return: List of all factors
    """
    check = 1
    factors = []
    while check < num/2+1:
        if num%check == 0:
            factors.append(check)
        check += 1
    factors.append(num)

    return factors


def all_factors_efficient(num):
    """
    Taken from:
    https://www.rookieslab.com/posts/most-efficient-way-to-find-all-factors-of-a-number-python-cpp#efficient-python-implementation-to-find-factors-of-a-number
    :param num: Number to find factors of
    :return: list of all factors
    """
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i * i <= num:
        # Check if i divides num without leaving a remainder
        if num % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if num // i != i:  # In Python, // operator performs integer/floored division
                result.append(num // i)
        i += 1
    # Return the list of factors of x
    return result

def next_fib(n_minus_1, n_minus_2):
    """
    Returns the next Fibonacci number given the previous two.
    :param n_minus_1: The last number
    :param n_minus_2: The number before last
    :return: The next number in a Fibonacci sequence.
    """
    assert n_minus_1 <= n_minus_2, f"n_minus_1 ({n_minus_1}) must be smaller than or equal to n_minus_2 ({n_minus_2})."
    return n_minus_1+n_minus_2


def hacky_big_factors(x):
    """
    Return the biggest factors of a number.
    Does not return all factors
    :param x: Number to return factors of
    :return: List of big factors
    """
    temp = x
    check = 2
    factors = [0]
    while temp > max(factors):
        if temp%check == 0:
            temp = temp / check
            factors.append(check)
        check += 1
    factors.remove(0)

    return factors


def is_palindrome(num:int) -> bool:
    """
    Returns a bool for whether a number is a palindrome.
    :param num: Number as an int
    :return: Bool decision
    """
    string_num = str(num)
    for i in range(int(len(string_num)/2)):
        if string_num[i] != string_num[len(string_num)-(i+1)]:
            return False

    return True


def triangle_number(size):
    """
    Return the triangle number of depth size
    :param size: depth of triangle
    :return: Triangle number
    """
    return sum(range(1, size+1))