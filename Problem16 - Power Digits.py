ANSWER = 1366
INPUT = 1000


def main(n):
    """Sum the digits for 2 to the power of a given number"""
    return sum([int(x) for x in str(2**n)])


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The sum of the digits of 2^{INPUT} is {answer}")
