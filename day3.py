import sys
import math
from mainUtils import read_input

# Find the largest battery from between start and end, inclusive
def find_largest_battery(bank, start, end):
    max_val = -1
    max_index = -1
    for i in range(start, end):
        if bank[i] > max_val:
            max_val = bank[i]
            max_index = i
    return max_index

# First battery in a bank is the left most highest number, ignoring the last one
# Last index (e.g. 12113) (the 3) can't be the first battery, since there's no second battery to the right
def find_first_battery_index(bank):
    return find_largest_battery(bank, 0, len(bank) - 1)

# Second battery is simply the largest number after the index of the first battery
def find_second_battery_index(bank, first_bat):
    return find_largest_battery(bank, first_bat+1, len(bank))

# Find the largest subset of batteries of size X in bank
def find_largest_battery_subset(bank, size):
    subset = ""
    start = 0

    for i in range(0,size):
        next_bat = find_largest_battery(bank, start, (len(bank) - size + 1 + i))
        subset += str(bank[next_bat])
        start = next_bat + 1
    return int(subset)

def day3(filename):
    print("aoc2025 day3")
    data = read_input(filename)
    
    # Part A, size 2
    total_joltage_a = 0
    total_joltage_b = 0
    for bank in data:
        bat_list = list(map(int, bank))
        print(bat_list)
        joltage = find_largest_battery_subset(bat_list, 2)
        print("Joltage A: "+str(joltage)) 
        total_joltage_a += joltage
        joltage_b = find_largest_battery_subset(bat_list, 12)
        print("Joltage B: "+str(joltage_b)) 
        total_joltage_b += joltage_b
        
    print("Total Joltage (part a): "+str(total_joltage_a))
    print("Total Joltage (part b): "+str(total_joltage_b))
    
if __name__ == "__main__":
    filename = "input/day3.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day3(filename)
