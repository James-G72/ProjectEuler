
def main(n):
    return sum([int(x) for x in str(2**1000)])


if __name__ == "__main__":
    p = 1000
    answer = main(p)
    print(f"The sum of the digits of 2^{p} is {answer}")
