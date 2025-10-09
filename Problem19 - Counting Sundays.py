import datetime as dt

ANSWER = 171
INPUT = None

START = dt.date(year=1901, month=1, day=1)
END = dt.date(year=2000, month=12, day=31)


def main(n):
	counter = 0
	day = START
	while day <= END:
		if day.weekday() == 6 and day.day == 1:
			counter += 1
		day += dt.timedelta(days=1)

	return counter


if __name__ == "__main__":
	answer = main(INPUT)
	print(f"The number of Sundays between {START.strftime('%d-%m-%Y')} and {END.strftime('%d-%m-%Y')} is {answer}")
