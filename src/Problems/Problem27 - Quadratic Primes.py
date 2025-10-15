"""
Was stuck with a 20-second solution so looked on the thread at how people had approached it.
Key things I had missed:
 - Not only does b have to be positive for the n=0 case, it must also be prime.
 - When n=1, p = 1 + a + b. All primes are odd except 2. Given the above line that b must be prime,
       then the only case that a can be odd, is when b is 2. All other cases a must be even, and
       therefore not prime, unless it also equals two.
To take advantage of the first thing, we can initialise the prime generator to have all primes up to 1000
and then iterate b through that range.
To take advantage of the second finding we want to make a the inner loop and only check odd values that are odd
unless b is 2.
"""
import GeneralFunctions as gf
import itertools

ANSWER = -59231
INPUT = None


class CheckPrimeWithGen():
    """Use a generator object to check if a value is prime."""
    def __init__(self):
        self.max_prime = 0
        self.primes = []
        self.prime_gen = gf.prime_generator_with_cache()
        while self.max_prime < 10:
            self._next_prime()

    def _next_prime(self):
        prime = next(self.prime_gen)
        self.max_prime = prime
        self.primes.append(prime)

    def check_prime(self, value):
        while value > self.max_prime:
            self._next_prime()
        return value in self.primes


def main(n):
    """Return the values for a and b such that the function n^2 + an + b produces the most primes."""
    max_run = 0
    best = (None, None)
    prime_checker = CheckPrimeWithGen()
    # Generate all primes up to 1000
    prime_checker.check_prime(1000)
    # Drop the last value as prime_checker will have generated the next prime larger than 1000
    for b in prime_checker.primes[:-1]:
        for a in range(-999, 1000, 2 if b !=2 else 1):
            count = 0
            for n in itertools.count():
                result = n**2 + a * n + b
                if not prime_checker.check_prime(result):
                    break
                count += 1
            if count > max_run:
                best = (a, b)
                max_run = count
    return best[0] * best[1]


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The longest recurring sequence for 1/n where n < {INPUT} is {answer}")
