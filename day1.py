import sys
import math
from mainUtils import read_input

def spin_dial(dial, command):
    direction = command[0]
    distance = int(command[1:])
    
    # Part b: How many times does the dial hit 0 as we turn?
    turn_zeroes = 0

    # Spin left, below 0, we wrap around
    if direction == "L":
        newdial = dial - distance
        if dial == 0:
            turn_zeroes -= 1
        dial = newdial % 100
        if newdial < 0:
            turn_zeroes += math.ceil(-newdial / 100)

    # Spin right, and wrap around 
    elif direction == "R":
        newdial = dial + distance
        dial = newdial % 100
        if newdial > 99:
            turn_zeroes = math.floor(newdial / 100)
            if dial == 0:
                turn_zeroes -= 1
            
    if dial == 0: 
        turn_zeroes += 1
    return dial, turn_zeroes

def day1(filename):
    print("aoc2025 day1")
    data = read_input(filename)
    
    dial = 50
    zeroes = 0
    all_zeroes = 0
    for command in data:
        dial, turn_zeroes = spin_dial(dial, command)
        print("Dial spun "+command+" to "+str(dial)+" hitting zero "+str(turn_zeroes)+" times")
        if dial == 0:
            zeroes += 1
        all_zeroes += turn_zeroes
            
    print("The dial hit 0 "+str(zeroes)+" times directly (part a)")
    print("The dial hit 0 "+str(all_zeroes)+" times in total (part b)")
    
if __name__ == "__main__":
    day1("input/day1.txt")
