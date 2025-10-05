

def main(n):
    count = 0
    for num in range(1, n+1):
        if num*num%2:
            count += num*num
    return count



if __name__ == "__main__":
    n = 704000
    answer = main(n)
    print(f"Sum of odd numbers in the first {n} square number is {answer}")