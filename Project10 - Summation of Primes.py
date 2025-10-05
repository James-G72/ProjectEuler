def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def main(n):
    prime_sum = 5
    for check in range(4, n):
        if len(prime_factors(check)) == 1:
            prime_sum += check

    return prime_sum

if __name__ == "__main__":
    n = 2000000
    answer = main(n)
    print(f"Sum of all primes below {n} is {answer}")
