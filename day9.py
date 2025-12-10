import math
import sys

from mainUtils import read_input_split
from shapely import Point, Polygon

def compute_area(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)

def find_largest_area(coords):
    max_area = 0
    
    for i in range(0, len(coords)):
        for j in range (i+1, len(coords)):
            area = compute_area(coords[i], coords[j])
            if max_area == 0 or area > max_area:
                max_area = area
    return max_area

def find_largest_intersecting_area(coords, poly):
    max_area = 0
    
    for i in range(0, len(coords)):
        for j in range (i+1, len(coords)):
            area = compute_area(coords[i], coords[j])
            print(str(coords[i])+" x "+str(coords[j])+"  Area: "+str(area))
            if max_area == 0 or area > max_area:
                                
                poly2 = Polygon((Point(coords[i][0], coords[i][1]), 
                                Point(coords[i][0], coords[j][1]),
                                Point(coords[j][0], coords[j][1]),
                                Point(coords[j][0], coords[i][1]),
                                Point(coords[i][0], coords[i][1])))
                p_contains = poly.contains(poly2)
                print("Contains: "+str(p_contains))
                    
                if p_contains:
                    print("Found enclosed polygon: "+str(coords[i])+","+str(coords[j])+" area = "+str(area))
                    max_area = area
    return max_area
                
def day9(filename):
    print("aoc2025 day9")
    coords = read_input_split(filename, ",", numbers=True)
    print(coords)
    
    max_area = find_largest_area(coords)
    print("Max Area (part a): "+str(max_area))
    
    poly = Polygon(coords)
    print(poly)
    
    max_area = find_largest_intersecting_area(coords, poly)
    
    print("Max Area (part b): "+str(max_area))
    
        
if __name__ == "__main__":
    filename = "input/day9.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day9(filename)
