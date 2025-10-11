ANSWER = 1074
INPUT = None
ROWS = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def get_indexes_above(row, row_index):
    """Return the index of the values available to a given number in the triangle"""
    if row == 0: # The top row is invalid
        return None, None
    elif row_index == 0: # If its the first index in the row then it can only see the other first index
        return 0, None
    elif row_index+1 == len(ROWS[row]): # Similar for the end
        return len(ROWS[row-1])-1, None
    else: # All other cases
        return row_index-1, row_index


def main(n):
    """Find the largest sum by navigating the triangle from top to bottom."""
    add_rows = []
    for row in range(0, len(ROWS)):
        add_row = []
        if row == 0:
            add_row.append(ROWS[row][0])
        else:
            for idx, value in enumerate(ROWS[row]):
                indexes_available = get_indexes_above(row, idx)
                options = [add_rows[row-1][x] for x in indexes_available if x is not None]
                add_row.append(value+max(options))
        add_rows.append(add_row)

    return max(add_rows[-1])


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The highest sum path through the triangle is {answer}")
