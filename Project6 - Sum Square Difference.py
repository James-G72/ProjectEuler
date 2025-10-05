def main():
    sum_nums = 0
    square_sum = 0
    for i in range(101):
        sum_nums += i
        square_sum += i**2
    square_total_sum = sum_nums**2
    difference = square_total_sum-square_sum

    return difference

if __name__ == "__main__":
    difference = main()
    print(f"The square difference of the first 100 numbers is {difference}")
