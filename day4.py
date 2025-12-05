import sys
import math
from mainUtils import read_input, print_grid, get_cell, create_grid
import copy

def is_movable(grid, x, y):
    nbr = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            cell = get_cell(grid, x + dx, y + dy)
            if cell == "@":
                nbr += 1
    return nbr < 4

def remove_paper(orig_grid):
    movable_grid = copy.deepcopy(orig_grid)
    movable_count = 0
    for y in range(0,len(orig_grid)):
        for x in range(0,len(orig_grid[y])):
            if orig_grid[y][x] == "@" and is_movable(orig_grid, x, y):
                movable_grid[y][x] = "."
                movable_count += 1
    return movable_grid, movable_count
                
def day4(filename):
    print("aoc2025 day4")
    orig_grid = create_grid(read_input(filename))
    
    movable_grid, movable_count = remove_paper(orig_grid)
    
    print_grid(movable_grid)
    print("Movable Paper Rolls (part a): "+str(movable_count))
    
    new_movable_count = movable_count
    index = 0
    while new_movable_count > 0:
        print("Step "+str(index))
        movable_grid, new_movable_count = remove_paper(movable_grid)
        movable_count += new_movable_count
        index += 1
        print_grid(movable_grid)
    
    print("After "+str(index)+" steps, paper rolls removed (part b): "+str(movable_count))
    
if __name__ == "__main__":
    filename = "input/day4.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day4(filename)
