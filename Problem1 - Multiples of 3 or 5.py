ANSWER = 233168
INPUT = 1000

def main(n):
    count = 0
    for num in range(1, n):
        if num % 3 == 0  or num % 5 == 0:
            count += num
    return count



if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Sum of multiples of 3 or 5 under {INPUT} is {answer}")