import GeneralFunctions as gf

ANSWER = 4782
INPUT = 1000


def main(n):
    """Returns the first fibonaci number to have n digits."""
    prev = 2
    prev_prev = 1
    fib = 3
    count = 3
    while len(str(fib)) < n:
        fib = gf.next_fib(prev, prev_prev)
        prev_prev = prev
        prev = fib
        count += 1

    return count


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The {INPUT}th permutation of the digits 0,1,2,3,4,5,6,7,8,9 is {answer}")
