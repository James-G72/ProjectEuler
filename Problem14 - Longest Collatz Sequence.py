ANSWER = 837799
INPUT = 1000000


def return_collatz(num):
    if num%2 == 0:
        return num/2
    else:
        return 3 * num + 1


def main(n):
    cache = {1:0}
    for start in range(2, n+1):
        num = start
        counter = 1
        while True:
            if num in cache.keys():
                break
            num = return_collatz(num)
            counter += 1
        cache[start] = cache[num] + counter

    return max(cache, key=cache.get)


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The starting value (below {INPUT}) with the largest chain is {answer}")
