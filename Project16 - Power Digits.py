ANSWER = 1366
INPUT = 1000


def main(n):
    return sum([int(x) for x in str(2**n)])


if __name__ == "__main__":
    answer = main(1000)
    print(f"The sum of the digits of 2^{1000} is {answer}")
