from pkg_resources._vendor.jaraco.context import null

# Load puzzle input into array from file, without newlines
def read_input(filename):
    with open(filename, 'r') as file:
        input_line = [line.strip() for line in file]
    return input_line

# Load puzzle input into two arrays from file, without newlines
# A single empty line separates the input into the two arrays
def read_input_two_sections(filename):
    with open(filename, 'r') as file:
        input1 = []
        input2 = []
        section1 = True
        for line in file:
            input_line = line.strip()
            if len(input_line) == 0:
                section1 = False
                continue
            if section1:
                input1.append(input_line)
            else:
                input2.append(input_line)

    return input1, input2

# Parse range "X-Y" -> X,Y as numbers
def parse_range(range_string):
    range_val = range_string.split("-")
    return int(range_val[0]), int(range_val[1])


# create a 2d grid (list of lists) from input data which is a list of strings
#  Each character in the input list string is a column
# ["abc","def"] -> [['a','b','c'],['d','e','f']]
def create_grid(data):
    grid = []
    for i in range(0, len(data)):
        row = []
        for j in range(0, len(data[i])):
            row.append(data[i][j])
        grid.append(row)
    return grid

# Write out a grid as a string 
def print_grid(data):
    for i in range(0, len(data)):
        row = ""
        for j in range(0, len(data[i])):
            row += str(data[i][j])
        print(row)    

# Given x/y coordinate, get the grid element at that location
# Return null if x/y is outside the grid
def get_cell(data, x, y):
    if y < 0 or y >= len(data):
        return null
    row = data[y]
    if x < 0 or x >= len(row):
        return null
    return row[x]
