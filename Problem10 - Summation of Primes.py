import GeneralFunctions as gf

ANSWER = 142913828922
INPUT = 2000000


def main(n):
    """Sum all the prime number below a given value."""
    prime_sum = 5
    for check in range(4, n):
        if gf.check_prime(check):
            prime_sum += check

    return prime_sum


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Sum of all primes below {INPUT} is {answer}")
