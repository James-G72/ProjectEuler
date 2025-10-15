from collections import OrderedDict

ANSWER = 983
INPUT = 1000


def long_div_for_remainder(top, bottom, dec_limit=20):
    """
    Perform a manual long division step process to decimalise a fraction top/bottom.
    :param top: Top value of the fraction
    :param bottom: Bottom value of the fraction
    :param dec_limit: Decimal place limit to return at
    :return: Fraction in decimal form.
    """
    assert top <= bottom, "Only works for fractions."
    dividend = top
    divisor = bottom
    number = ""
    decimal_cache = OrderedDict()
    recur_out = 0
    counter = 0
    while counter < dec_limit+1:
        quotient, remainder = divmod(dividend, divisor)
        # Check if we have come to a half
        if quotient == 0 and remainder == 0:
            break
        # Check for carrying
        if remainder < divisor:
            dividend = remainder * 10
        else:
            dividend = remainder
        # Check if the current state has been seen before
        if (dividend,divisor) in decimal_cache.keys():
            # Subtracting 1 for the index offset in counter
            start_idx = decimal_cache[(dividend,divisor)] - 1
            recur_out = number.split(".")[-1][start_idx:]
            break
        elif "." in number:
            decimal_cache[(dividend,divisor)] = counter
        # Add the quotient to the number
        if counter == 0:
            number += "0."
        else:
            number += str(quotient)
        counter += 1

    return float(number), int(recur_out)


def main(n):
    """Return the value d for which 1/d has the longest recurring cycle in its decimal representation."""
    longest_recurring = 0
    for div in range(2, n):
        _, recur = long_div_for_remainder(1, div, dec_limit=10000)
        if len(str(recur)) > longest_recurring:
            longest_recurring = div

    return longest_recurring


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The longest recurring sequence for 1/n where n < {INPUT} is {answer}")
