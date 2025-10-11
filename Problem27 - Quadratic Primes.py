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
    for a in range(-999, 1000):
        # We can start b from only positive as n = 0 will never be positive if b isn't
        for b in range(0, 1001):
            count = 0
            for n in itertools.count():
                result = n**2 + a * n + b
                if result <= 0:
                    break
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
