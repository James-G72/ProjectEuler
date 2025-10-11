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
    decimals = -1
    dividend = top
    divisor = bottom
    number = ""
    decimal_cache = OrderedDict()
    recurr_out = 0
    while decimals < dec_limit:
        quotient, remainder = divmod(dividend, divisor)
        if quotient == 0 and remainder == 0:
            break
        if remainder < divisor:
            dividend = remainder * 10
        else:
            dividend = remainder
        if (dividend,divisor) in decimal_cache.keys():
            start_idx = decimal_cache[(dividend,divisor)]
            recurr_out = number.split(".")[-1][start_idx:]
            break
        elif "." in number:
            decimal_cache[(dividend,divisor)] = decimals
        if decimals == -1 and quotient == 0:
            number += "0."
            decimals = 0
        else:
            number += str(quotient)
            if decimals >= 0:
                decimals += 1

    return float(number), int(recurr_out)


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
    print(f"The longest recurring sequence for 1/n where n < {INPUT} is {answer} digits")
