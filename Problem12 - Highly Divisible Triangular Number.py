import GeneralFunctions as gf

ANSWER = 76576500
INPUT = 500

def main(n):
    """A triangle number is the sum of all numbers up to n. Find the first triangle number that has over 500 divisors."""
    factors = []
    tri_number = 1
    counter = 2
    while len(factors) < n:
        tri_number += counter
        factors = gf.all_factors_efficient(tri_number)
        counter += 1

    return tri_number


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"First triangle number with over {INPUT} factors is {answer}")
