ANSWER = 21124
INPUT = 1000
NUM_DICT = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
            90: "Ninety", 100: "OneHundred", 1000: "OneThousand"}


def number_as_word(n):
    """Only works up to 1000"""
    assert n <= 1000, "Can only sum numbers below 1000."
    if n in NUM_DICT.keys():
        return NUM_DICT[n]
    elif n >= 100:
        if n % 100 == 0:
            return f"{number_as_word(int(str(n)[0]))}Hundred"
        else:
            return f"{number_as_word(int(str(n)[0]))}Hundredand{number_as_word(int(str(n)[1:]))}"
    else:
        return f"{number_as_word(n-n%10)}{number_as_word(n%10)}"


def main(n, print_ans=False):
    total_letters = 0
    for num in range (1, n+1):
        total_letters += len(number_as_word(num))
        if print_ans:
            print(number_as_word(num))

    return total_letters


if __name__ == "__main__":
    answer = main(INPUT, print_ans=True)
    print(f"The total number of letters needed to count to {INPUT} is {answer}")
