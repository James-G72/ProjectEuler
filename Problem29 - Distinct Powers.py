ANSWER = 9183
INPUT = 100


def main(n):
    """Distinct terms in a^b for a and b varied from 2 to n"""
    out_set = set()
    for a in range(2, n+1):
        for b in range(2, n+1):
            out_set.add(a**b)

    return len(out_set)


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The number of distinct values of a^b for 2<a<{INPUT} and 2<b<{INPUT} is {answer}")
