def get_factors(x):
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


def main(n):
    all_factors = get_factors(n)
    prime_factors = []
    print(all_factors)
    for factor in all_factors:
        if len(get_factors(factor)) == 1:
            prime_factors.append(factor)
    return max(prime_factors)


if __name__ == "__main__":
    n = 600851475143
    answer = main(n)
    print(f"Largest prime factor of {n} is {answer}")