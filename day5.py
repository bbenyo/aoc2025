import sys
import math
from mainUtils import read_input_two_sections, parse_range

def is_fresh(id, ranges):
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            return range
    return None

def get_range_no_overlap(range, nor):
    # Range starts after other range ends
    if range[0] > nor[1]:
        return None
    # Range ends before other range begins
    if range[1] < nor[0]:
        return None
    # They overlap, beginning of the new range to beginning of the existing one is new
    n_ranges = []
    if range[0] < nor[0]:
        start1 = range[0]
        end1 = nor[0] - 1
        n_ranges.append((start1, end1))
    
    if range[1] > nor[1]:
        # end of the old range to end of the new is new
        start2 = nor[1] + 1
        end2 = range[1]
        n_ranges.append((start2, end2))
        
    return n_ranges
                   
def day5(filename):
    print("aoc2025 day5")
    range_strs,ids = read_input_two_sections(filename)
    
    ranges = []
    for range in range_strs:
        ranges.append(parse_range(range))
    
    print("Ranges:")
    print(ranges)
    
    fresh_count = 0
    for id in ids:
        fresh_range = is_fresh(int(id), ranges)
        if fresh_range is not None:
            print(id+" is fresh: "+str(fresh_range))
            fresh_count += 1
        else:
            print(id+" is NOT fresh")
    
    print("Fresh count (part a): "+str(fresh_count))
    
    # Part B: Create a non-overlapping list of ranges, then simply get each range size
    # "Insertion sort", for each new range, keep splitting it until we get a set of non-overlapping ranges
    no_ranges = []
    for range in ranges:
        insert_range = []
        insert_range.append(range)
        while len(insert_range) > 0:
            irange = insert_range.pop(0)
            print("Inserting "+str(irange))
            add_me = True
            for nor in no_ranges:
                # Parts of the range that don't overlap, None or 1 or 2 ranges (before start, after end)
                no_overlap = get_range_no_overlap(irange, nor)
                if no_overlap is not None:
                    add_me = False
                    for o_rng in no_overlap:
                        print("Non overlapping portion: "+str(o_rng)+" with "+str(nor))
                        insert_range.append(o_rng)
                    break
            if add_me:
                print("Adding "+str(irange))
                no_ranges.append(irange)
    
    no_ranges.sort()
    print("Non Overlapping Ranges: "+str(no_ranges))    
    
    # Count the range sizes
    total = 0
    for range in no_ranges:
        total += (range[1] - range[0] + 1)
    
    print("Total Fresh IDs: "+str(total))
    
    
if __name__ == "__main__":
    filename = "input/day5.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day5(filename)
