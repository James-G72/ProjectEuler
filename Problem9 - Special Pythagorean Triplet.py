ANSWER = 31875000
INPUT = 1000

def main(n, print_ans=False):
    """Find the values of a,b and c, such that a^2+b^2+=c^2 and a+b+c=1000. Return a*b*c."""
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a < b < c and a + b + c == n and a*a + b*b == c*c:
                    if print_ans:
                        print(f"a = {a}, b = {b}, c = {c}")
                    return a*b*c
    return False

if __name__ == "__main__":
    answer = main(INPUT, print_ans=True)
    print(f"Product that satisfies all conditions is {answer}")
