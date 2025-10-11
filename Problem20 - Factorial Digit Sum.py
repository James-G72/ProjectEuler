import GeneralFunctions as gf

ANSWER = 648
INPUT = 100


def main(n):
    """Sum all the digits in the factorial of a given number."""
    return sum([int(x) for x in str(gf.factorial(n))])


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The sum of the digits of {INPUT}! is {answer}")
