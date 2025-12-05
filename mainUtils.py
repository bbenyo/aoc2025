from pkg_resources._vendor.jaraco.context import null

# Load puzzle input into array from file, without newlines
def read_input(filename):
    with open(filename, 'r') as file:
        input_line = [line.strip() for line in file]
    return input_line

def create_grid(data):
    grid = []
    for i in range(0, len(data)):
        row = []
        for j in range(0, len(data[i])):
            row.append(data[i][j])
        grid.append(row)
    return grid

def print_grid(data):
    for i in range(0, len(data)):
        row = ""
        for j in range(0, len(data[i])):
            row += str(data[i][j])
        print(row)    

def get_cell(data, x, y):
    if y < 0 or y >= len(data):
        return null
    row = data[y]
    if x < 0 or x >= len(row):
        return null
    return row[x]
