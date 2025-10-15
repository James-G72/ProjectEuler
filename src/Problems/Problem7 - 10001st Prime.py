import GeneralFunctions as gf

ANSWER = 104743
INPUT = 10001

def main(n):
    """Find the nth prime number."""
    found = 1
    number = 1
    while found != n:
        number+=2
        if len(gf.prime_factors(number)) == 1:
            found += 1

    return number

if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Prime number {INPUT} is {answer}")
