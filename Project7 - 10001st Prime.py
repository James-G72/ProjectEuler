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
    found = 1
    number = 1
    while found != n:
        number+=2
        if len(prime_factors(number)) == 1:
            found += 1

    return number

if __name__ == "__main__":
    n = 10001
    answer = main(n)
    print(f"Prime number {n} is {answer}")
