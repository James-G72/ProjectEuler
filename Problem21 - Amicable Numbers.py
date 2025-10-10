import GeneralFunctions as gf

ANSWER = 31626
INPUT = 10000


def main(n):
	total_count = 0
	for num in range(1, n+1):
		factor_sum = sum(sorted(gf.all_factors_efficient(num))[:-1])
		if sum(sorted(gf.all_factors_efficient(factor_sum))[:-1]) == num and factor_sum != num:
			total_count += num

	return total_count


if __name__ == "__main__":
	answer = main(INPUT)
	print(f"The sum of the digits of {INPUT}! is {answer}")
