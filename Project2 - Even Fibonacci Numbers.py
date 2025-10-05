
def next_fib(prev, prev_prev):
    return prev+prev_prev

def main(n):
    prev = 2
    prev_prev = 1
    count = 2
    fib = 3
    while fib <= n:
        fib = next_fib(prev, prev_prev)
        if not fib%2:
            count += fib
        prev_prev = prev
        prev = fib
    return count

if __name__ == "__main__":
    n = 4000000
    answer = main(n)
    print(f"Sum of even fibonacci numbers under {n} is {answer}")