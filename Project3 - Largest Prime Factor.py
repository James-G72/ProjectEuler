import GeneralFunctions as gf


def main(n):
    all_factors = gf.hacky_big_factors(n)
    prime_factors = []
    print(all_factors)
    for factor in all_factors:
        if len(gf.hacky_big_factors(factor)) == 1:
            prime_factors.append(factor)
    return max(prime_factors)


if __name__ == "__main__":
    n = 600851475143
    answer = main(n)
    print(f"Largest prime factor of {n} is {answer}")