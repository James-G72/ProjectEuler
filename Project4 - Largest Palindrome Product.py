import GeneralFunctions as gf

ANSWER = 906609
INPUT = 3

def main(n):
    palindromes = 0
    for num1 in range(10**(n-1), 10**n):
        for num2 in range(10**(n-1),10**n):
            product = num1*num2
            if gf.is_palindrome(product):
                if product>palindromes:
                    palindromes = product
    return palindromes


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The largest palindrome made from the product of two {INPUT}-digit numbers is {answer}")