import GeneralFunctions as gf


def main(n):
    prime_sum = 5
    for check in range(4, n):
        if len(gf.prime_factors(check)) == 1:
            prime_sum += check

    return prime_sum


if __name__ == "__main__":
    n = 2000000
    answer = main(n)
    print(f"Sum of all primes below {n} is {answer}")
