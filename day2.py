import sys
import math
from mainUtils import read_input

invalid_ids = []
largest_range = 0

# Get the next possible invalid id after number, inclusive
def get_next_invalid(number, repetitions):
    number_str = str(number)
    # next possible is the first nth of the number, duplicated, e.g. 1234 -> 1212
    size = len(number_str)
    if size % repetitions == 0:
        digits = math.floor(size / repetitions)
        half_str = number_str[0:digits]
        next_inv_str = half_str
        for _ in range(1,repetitions):
            next_inv_str += half_str
        next_inv = int(next_inv_str)
        
        if next_inv < number:
            half = int(half_str) + 1
            half_str = str(half)
            next_inv_str = half_str
            for _ in range(1,repetitions):
                next_inv_str += half_str
            next_inv = int(next_inv_str)
                
        # print("  next_invalid = "+str(next_inv))
        return next_inv
    else:
        # No odd number can be invalid (invalid = sequence of n identical numbers)
        # Next possible has to be next even (1000X)
        return get_next_invalid(round(math.pow(10, size)), repetitions)


# is the given id (invalid) in the range? (start - end)
def in_range(invalid, range_start, range_end):
    return invalid >= range_start and invalid <= range_end

# Find all invalid IDs in a range by computing the next possible invalid id from start and checking if it's still in the range
def find_invalid(range_string, repetitions):
    range_val = range_string.split("-")
    range_start = int(range_val[0])
    range_end = int(range_val[1])
    global largest_range
    
    if range_end > largest_range:
        largest_range = range_end
    
    # Find first possible invalid ID after start
    # print("Range: "+str(range_start)+" - "+str(range_end))
    invalid = get_next_invalid(range_start, repetitions)
    while in_range(invalid, range_start, range_end):
        print("Found invalid id "+str(invalid)+" in "+range_string)
        if invalid in invalid_ids:
            print("  But we already have that one")
        else:
            invalid_ids.append(invalid)
        invalid = get_next_invalid(invalid + 1, repetitions)

def day2(filename):
    print("aoc2025 day2")
    data = read_input(filename)
    global invalid_ids
    
    ranges = data[0].split(",");
    
    for range_string in ranges:
        find_invalid(range_string, 2)
        
    print("Invalid IDs with 2 sequences: "+str(invalid_ids))
    total = 0
    for invalid in invalid_ids:
        total += invalid
    print("Added invalid ids with 2 sequences (part a): "+str(total))
    
    all_invalid_ids = []
    all_invalid_ids.extend(invalid_ids)
        
    for i in range(3, len(str(largest_range))):
        invalid_ids = []
        for range_string in ranges:
            find_invalid(range_string, i)
        print("Invalid IDs with "+str(i)+" sequences: "+str(invalid_ids))
        for invalid in invalid_ids:
            if invalid not in all_invalid_ids:
                all_invalid_ids.append(invalid)
                total += invalid
                
    print("All Invalid Ids: "+str(all_invalid_ids))
    print("Total invalid ids (part b): "+str(total))
    
if __name__ == "__main__":
    filename = "input/day2.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day2(filename)
