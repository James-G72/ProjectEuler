ANSWER = 58152277333216000
INPUT = 704000

def main(n):
    count = 0
    for num in range(1, n+1):
        if num*num%2:
            count += num*num
    return count


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Sum of odd numbers in the first {INPUT} square number is {answer}")