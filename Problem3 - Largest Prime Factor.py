import GeneralFunctions as gf

ANSWER = 6857
INPUT = 600851475143


def main(n):
    """Calculate the largest prime factor for a given number."""
    all_factors = gf.hacky_big_factors(n)
    prime_factors = []
    for factor in all_factors:
        if len(gf.hacky_big_factors(factor)) == 1:
            prime_factors.append(factor)
    return max(prime_factors)


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Largest prime factor of {INPUT} is {answer}")