import GeneralFunctions as gf

ANSWER = 142913828922
INPUT = 2000000


def sieve_of_eratosthenes(num):
    sieve = [True] * num
    for p in range(2, num):
        if sieve[p]:
            for multiple in range(p * p, num, p):
                sieve[multiple] = False
    # 1 is not prime
    sieve[1] = False
    # Throughout, index was treated as number, we therefore drop the first index 0
    return sieve[1:]


def main(n):
    """Sum all the prime numbers below a given value."""
    prime_sieve = sieve_of_eratosthenes(n)
    # As we now want to represent index as numbers we need to add one
    return sum([idx+1 for idx, check in enumerate(prime_sieve) if check])


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Sum of all primes below {INPUT} is {answer}")
