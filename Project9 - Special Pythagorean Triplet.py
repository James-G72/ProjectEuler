

def main(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a < b and b < c and a + b + c == n and a*a + b*b == c*c:
                    print(f"a = {a}, b = {b}, c = {c}")
                    return a*b*c
    return False

if __name__ == "__main__":
    n = 1000
    answer = main(n)
    print(f"Product that satisfies all conditions is {answer}")
