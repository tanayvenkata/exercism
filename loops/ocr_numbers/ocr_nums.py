def convert(input_grid):
    new_set = []
    binary_str = ""

    while input_grid:
        new_set.append(input_grid[:4])
        input_grid = input_grid[4:]

    for row in new_set:
        binary_str += part_convert(row)
        binary_str += ","

    return binary_str[:-1]


def part_convert(input_grid):
    check_input(input_grid)

    binary_str = ""
    for i in range(0, len(input_grid[0]), 3):  # grabs 3-size chunks from input grid
        number = []
        for row in input_grid:
            number.append(row[i : i + 3])
        binary_str += convert_num(number)
    return binary_str


def convert_num(number):
    ocr_nums = {
        (" _ ", "| |", "|_|", "   "): "0",
        ("   ", "  |", "  |", "   "): "1",
        (" _ ", " _|", "|_ ", "   "): "2",
        (" _ ", " _|", " _|", "   "): "3",
        ("   ", "|_|", "  |", "   "): "4",
        (" _ ", "|_ ", " _|", "   "): "5",
        (" _ ", "|_ ", "|_|", "   "): "6",
        (" _ ", "  |", "  |", "   "): "7",
        (" _ ", "|_|", "|_|", "   "): "8",
        (" _ ", "|_|", " _|", "   "): "9",
    }
    return ocr_nums.get(tuple(number), "?")


def check_input(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
