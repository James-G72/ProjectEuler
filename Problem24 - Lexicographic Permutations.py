import itertools

import GeneralFunctions as gf

ANSWER = 2783915460
INPUT = 1000000


def return_start_digit(digits, num):
    total_permutations = gf.permutation_count(digits,repeats=False)
    div, mod = divmod(num, total_permutations/len(digits))
    # Catches the case where it is the last example of a given permutation
    if mod == 0:
        div -= 1
    return digits[int(div)], mod


def main(n):
    """Returns the nth Lexicographic Permutation of the digits 0 to 9 inclusive."""
    digits = "0123456789"
    out_str = ""
    remainder = n
    while len(digits) > 0:
        new_digit, remainder = return_start_digit(digits, remainder)
        out_str += new_digit
        digits = digits.replace(new_digit, "")

    return out_str


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The {INPUT}th permutation of the digits 0,1,2,3,4,5,6,7,8,9 is {answer}")
