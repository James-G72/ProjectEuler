import GeneralFunctions as gf


def main(n):
    factors = []
    tri_number = 1
    counter = 2
    while len(factors) < n:
        tri_number += counter
        factors = gf.all_factors_efficient(tri_number)
        counter += 1

    return tri_number


if __name__ == "__main__":
    n = 500
    answer = main(n)
    print(f"First triangle number with over {n} factors is {answer}")
