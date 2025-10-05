import GeneralFunctions as gf


def main():
    palindromes = 0
    for num1 in range(100, 1000):
        for num2 in range(100,1000):
            product = num1*num2
            if gf.is_palindrome(product):
                if product>palindromes:
                    palindromes = product
    return palindromes


if __name__ == "__main__":
    answer = main()
    print(f"The largest palindrome made from the product of two 3-digit numbers is {answer}")