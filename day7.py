import sys
import math
from mainUtils import read_input, create_grid, get_cell, print_grid

# Propagate the grid at row X
# S -> |, | moves down or gets split if it hits ^

# Part B: Count timelines
#  Count how many different ways there were to get to this row/column
def propagate_taychons(grid, row, timelines):
    splits = 0
    for i in range(0, len(grid[row])):
        cell = get_cell(grid, i, row)
        match (cell):
            case 'S' : 
                grid[row+1][i] = '|';
                timelines[i] = 1
            case '|' : 
                next_cell = get_cell(grid, i, row+1)
                match (next_cell):
                    case None: continue
                    case '.' : 
                        grid[row+1][i] = '|';
                    case '^' : # Split
                        # Creates 2 timelines, 1 to the left, 1 to the right
                        lcell = get_cell(grid, i-1, row+1)
                        if (lcell == '.'):
                            grid[row+1][i-1] = '|'
                        if (lcell is not None):
                            timelines[i-1] += timelines[i]
                        rcell = get_cell(grid, i+1, row+1)
                        if (rcell == '.'):
                            grid[row+1][i+1] = '|'
                        if (rcell is not None):
                            timelines[i+1] += timelines[i]
                        splits += 1
                        timelines[i] = 0
                    case '|': # do nothing
                        continue
    return splits
    
def day7(filename):
    print("aoc2025 day7")
    orig_grid = create_grid(read_input(filename))
    print_grid(orig_grid)
    
    timelines = [0] * len(orig_grid[0])
    
    total_splits = 0
    for i in range(0, len(orig_grid)-1):
        new_splits = propagate_taychons(orig_grid, i, timelines)
        total_splits += new_splits
        print("Step: "+str(i)+" Splits: "+str(new_splits))
        print_grid(orig_grid)
        print("Timelines: "+str(timelines))
        print("Timeline Count: "+str(sum(timelines)))
    
    print("Total Tachyon splits (part a): "+str(total_splits))
    
if __name__ == "__main__":
    filename = "input/day7.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day7(filename)
