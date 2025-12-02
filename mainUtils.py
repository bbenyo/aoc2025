
# Load puzzle input into array from file, without newlines
def read_input(filename):
    with open(filename, 'r') as file:
        input = [line.strip() for line in file]
    return input

