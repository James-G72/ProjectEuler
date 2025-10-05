import GeneralFunctions as gf


def main(n):
    found = 1
    number = 1
    while found != n:
        number+=2
        if len(gf.prime_factors(number)) == 1:
            found += 1

    return number

if __name__ == "__main__":
    n = 10001
    answer = main(n)
    print(f"Prime number {n} is {answer}")
