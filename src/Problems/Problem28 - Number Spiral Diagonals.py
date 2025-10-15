ANSWER = 669171001
INPUT = 1001


def corner_values_spiral(size, start, start_height):
    """
    Return the sum of the corner values of a spiral of size starting at start, where the spiral starts at start_height
    :param size: Length of one side of the grid
    :param start_height: Distance vertically up the spiral starts.
    :return: Sum of corner values
    """
    corner_1 = start+(start_height-1)
    corner_234 = 3 * (corner_1 + 2 * (size-1))

    return corner_1 + corner_234


def main(n):
    """Return the sum of all values on diagonals of a square grid with length n."""
    total_diags = 1
    last_value = 1
    for size in range(3, 1002, 2):
        height = size - 1
        total_diags += corner_values_spiral(size, last_value + 1, height)
        last_value += 2 * size + 2 * (size - 2)

    return total_diags


if __name__ == "__main__":
    answer = main(INPUT)
    print(f"The sum along the diagonals along an {INPUT}x{INPUT} grid is {answer}")
