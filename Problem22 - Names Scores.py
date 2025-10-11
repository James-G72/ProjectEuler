import GeneralFunctions as gf

ANSWER = 871198282
INPUT = r"/Users/jamesgower2/Documents/PycharmProjects/ProjectEuler/Test Data/0022_names.txt"


def txt_to_list(path):
    out_list = []
    with open(path, "r") as file:
        lines = file.readlines()
    strings = [x[1:-1] for x in lines[0].split(",")]

    return strings


def score_word(word):
    return sum([ord(x)-64 for x in word])


def main(p):
    """For a given list of names, score the names by multiplying their alphabetical rank by the sum of their letters by alphabetical position."""
    name_list = sorted(txt_to_list(p))

    total_count = 0
    for idx, name in enumerate(name_list):
        total_count += (idx+1)*score_word(name)

    return total_count


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The sum of the digits of {INPUT.split('/')[-1]}! is {answer}")
