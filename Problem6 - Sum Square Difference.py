ANSWER = 25164150
INPUT = 100

def main(n):
    sum_nums = 0
    square_sum = 0
    for i in range(n+1):
        sum_nums += i
        square_sum += i**2
    square_total_sum = sum_nums**2
    difference = square_total_sum-square_sum

    return difference

if __name__ == "__main__":
    difference = main(INPUT)
    print(f"The square difference of the first {INPUT} numbers is {difference}")
