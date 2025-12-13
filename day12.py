import math
import sys

from mainUtils import read_input

class Present:
    def __init__(self, index):
        self.ident = index
        self.grid = []
        # How many squares are filled in
        self.size = 0
        
    def __str__(self):
        ret = str(self.ident)+" size: "+str(self.size)+"\n"
        for i in range(0, len(self.grid)):
            ret += str(self.grid[i])+"\n"
        return ret
    
    def add_row(self, row):
        self.grid.append(row)
        for x in row:
            if x == '#':
                self.size += 1
        
class Region:
    def __init__(self, index, x, y, presents):
        self.id = index
        self.width = int(x)
        self.height = int(y)
        self.presents = presents
        
    def __str__(self):
        ret = str(self.width)+" x "+str(self.height)+": "
        for i in range(0, len(self.presents)):
            ret += str(self.presents[i])+","
        ret += " area: "+str(self.area())
        return ret
    
    def area(self):
        return self.width * self.height
    
    # is it possible to fit all presents inside
    def sanity_check(self, pres_list):
        total = 0
        for i in range(0, len(self.presents)):
            pres = pres_list[i]
            total += (pres.size * int(self.presents[i]))
        if total > self.area():
            print("Total Present area: "+str(total)+" > "+str(self.area()))
            return False
        return True
        

def day12(filename):
    print("aoc2025 day12")
    data = read_input(filename)
    
    presents = []
    regions = []
    cur_present = None
    for line in data:
        if ":" in line:
            id_line = line.split(":")
            ident = id_line[0]
            if "x" in ident:
                cur_present = None
                wh = ident.split("x")
                width = wh[0]
                height = wh[1]
                r_presents = id_line[1].split()
                region = Region(len(regions) - 1, width, height, r_presents)
                regions.append(region)
            else:
                cur_present = Present(ident)
                presents.append(cur_present)
        elif len(line) == 0:
            cur_present = None
        else:
            cur_present.add_row(line)
            
    for present in presents:
        print(str(present))
        
    sanity_passed = 0
    for region in regions:
        print(region)
        if region.sanity_check(presents):
            sanity_passed += 1
            
    # Start by eliminating ones that don't pass the sanity check via area
    print("Passed area sanity check: "+str(sanity_passed))
    
    # We could try to fit presents into regions now, but the number that pass the sanity check is the right answer
    # Christmas miracle!
            
if __name__ == "__main__":
    filename = "input/day12.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day12(filename)
