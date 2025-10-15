import GeneralFunctions as gf

ANSWER = 4613732
INPUT = 4000000

def main(n):
    """Sum all even Fibonacci numbers below a given value."""
    prev = 2
    prev_prev = 1
    count = 2
    fib = 3
    while fib <= n:
        fib = gf.next_fib(prev, prev_prev)
        if not fib%2:
            count += fib
        prev_prev = prev
        prev = fib
    return count

if __name__ == "__main__":
    answer = main(INPUT)
    print(f"Sum of even fibonacci numbers under {INPUT} is {answer}")