import GeneralFunctions as gf
import math

ANSWER = 4179871
INPUT = None


def check_abundant(num):
    all_factors = sorted(gf.all_factors_efficient(num))[:-1]
    return sum(all_factors) > num


def main(n):
    """Returns the sum of all positive integers which cannot be written as the sum of two abundant numbers."""
    abundants = [check_abundant(x) for x in range(1, 28123)]
    # Adding a 0th element to make indexing more intuitive
    abundants.insert(0, False)
    out_sum = 1
    for num in range(2, 28123):
        valid = False
        for num1 in range(1, math.ceil(num/2)+1):
            if abundants[num1] and abundants[num-num1]:
                valid =  True
                break
        if not valid:
            out_sum += num
    return out_sum



if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The sum numbers that can't be made from two abundant numbers is {answer}")
