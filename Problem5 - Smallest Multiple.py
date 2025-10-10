import copy
import GeneralFunctions as gf

ANSWER = 232792560
INPUT = 20

def check_covered(list1, list2):
    temp_list = copy.deepcopy(list2)
    needed = []
    for item in list1:
        if item in temp_list:
            temp_list.remove(item)
        else:
            needed.append(item)
    return needed


def main(n):
    full_list = []
    for x in range(1, n+1):
        full_list.extend(check_covered(gf.prime_factors(x), full_list))

    out = 1
    for x in full_list:
        out *= x

    return out

if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The smallest number that has 1 to {INPUT} as factors is {answer}")