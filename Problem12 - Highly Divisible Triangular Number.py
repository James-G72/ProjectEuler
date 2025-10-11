import GeneralFunctions as gf
import itertools
import functools
import collections

ANSWER = 76576500
INPUT = 500


def prime_generator_with_cache(_primes=[]):
    yield from _primes
    start = 2 if not _primes else _primes[-1]+1
    for candidate in itertools.count(start):
        for prime in _primes:
            if candidate % prime == 0:
                break
        else:
            yield candidate
            _primes.append(candidate)


def all_prime_factors(num):
    factors = collections.defaultdict(lambda: 0)
    for prime in prime_generator_with_cache():
        while num % prime == 0:
            factors[prime] += 1
            num /= prime
        if num == 1:
            break
    return factors


def tri_number_gen():
    tri = 0
    # Starting a counter at 1
    for i in itertools.count(1):
        tri += i
        yield tri


def main(n):
    """A triangle number is the sum of all numbers up to n. Find the first triangle number that has over 500 prime factors."""
    for tri_number in tri_number_gen():
        prime_factors = all_prime_factors(tri_number)
        num_divisors = functools.reduce(lambda a,b:a * b,map(lambda x:x+1,prime_factors.values()),1)
        if num_divisors > n:
            return tri_number
    return None

if __name__ == "__main__":
    answer = main(INPUT)
    print(f"First triangle number with over {INPUT} factors is {answer}")
