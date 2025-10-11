ANSWER = 443839
INPUT = 5


def power_sum(power, value):
    return sum([int(x)**power for x in str(value)])


def calc_upper_lim(power):
    n_digits = 1
    while n_digits * 9 ** power >= 10 ** n_digits:
        n_digits += 1

    return n_digits


def main(n):
    """Find the sum of all values that can be written as the sum of the 5th power of their digits"""
    # Ceiling for possible values is i * 9^n >= 10^i
    most_digits = calc_upper_lim(n)
    total_sum = 0
    counter = 2
    while counter <= most_digits * 9 ** 5:
        if counter == power_sum(n, counter):
            total_sum += counter
        counter += 1

    return total_sum


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The sum of all values that can be written as the sum of the {INPUT}th power of their digits {answer}")
