import sys
import math
from mainUtils import read_input_split
import bisect

def distance(box1, box2):
    return math.sqrt((box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2)

def find_closest_n(boxes, n):
    min_distance = []
    
    for i in range(0, len(boxes)):
        for j in range (i+1, len(boxes)):
            dist = distance(boxes[i], boxes[j])
            if len(min_distance) == 0 or dist < min_distance[len(min_distance)-1][0]:
                bisect.insort(min_distance, [dist, (i,j)])
                if len(min_distance) > n:
                    min_distance.remove(min_distance[len(min_distance) - 1])
    return min_distance

def find_circuit(box, circuits):
    for i in range(0, len(circuits)):
        if box in circuits[i]:
            return i
    print("Can't find: "+str(box))
                
def connect(closest_pair, circuits):
    circuit1 = find_circuit(closest_pair[0], circuits)
    circuit2 = find_circuit(closest_pair[1], circuits)
    # connect circuit 1 and 2
    if circuit1 == circuit2:
        # no-op, already connected
        print("Circuit "+str(circuits[circuit1])+" and "+str(circuits[circuit2])+" are already connected")
        return False
    # Make circuit1 the combined circuit
    for c in circuits[circuit2]:
        circuits[circuit1].append(c)
    circuits[circuit2] = []
    print("Connected "+str(circuit1)+" and "+str(circuit2)+" to form circuit "+str(circuit1)+": "+str(circuits[circuit1]))
    return True
    
def remove_largest(circuits):
    largest = 0
    largest_index = -1
    for i in range(0, len(circuits)):
        length = len(circuits[i])
        if length > largest:
            largest = length
            largest_index = i
            
    circuits[largest_index] = []
    return largest

def day8(filename):
    print("aoc2025 day8")
    boxes = read_input_split(filename, ",", numbers=True)
    print(boxes)
    
    day8_partA(boxes)
    day8_partB(boxes)
    
def day8_partA(boxes):
    connections = 0
    if filename.startswith("sample"):
        connections = 10
    else:
        connections = 1000
        
    circuits = dict()
    for i in range(0, len(boxes)):
        circuits[i] = [i]

    closest_pairs = find_closest_n(boxes, connections)
    for i in range(0, connections):
        closest_pair = closest_pairs.pop(0)
        pair = closest_pair[1]
        print("Closest Pair "+str(i)+" is "+str(boxes[pair[0]])+" - "+str(boxes[pair[1]]))
        connect(pair, circuits)
    
    print("Circuits:")    
    print(circuits)
    
    total = 1
    for i in range(0,3):
        largest = remove_largest(circuits)
        print("Largest "+str(i)+" circuit length: "+str(largest))
        total *= largest
        
    print("Three largest circuits (part a): "+str(total))
    
def is_all_one_circuit(circuits, max):
    for i in range(0, len(circuits)):
        length = len(circuits[i])
        if length > 0 and length < max:
            return False
    return True
    
def day8_partB(boxes):
    # TODO: Make this more efficient...
    box_count = len(boxes)
    connections = (box_count * box_count) / 2

    circuits = dict()
    for i in range(0, len(boxes)):
        circuits[i] = [i]

    closest_pairs = find_closest_n(boxes, connections)
    all_one_circuit = False
    pair = []
    
    while not all_one_circuit:
        closest_pair = closest_pairs.pop(0)
        pair = closest_pair[1]
        print("Closest Pair "+str(i)+" is "+str(boxes[pair[0]])+" - "+str(boxes[pair[1]]))
        connect(pair, circuits)
        all_one_circuit = is_all_one_circuit(circuits, box_count)
    
    print("Circuits:")    
    print(circuits)
    
    print("Last Pair: "+str(pair))
    box1 = boxes[pair[0]]
    box2 = boxes[pair[1]]
    total = box1[0] * box2[0]
    print("Box1: "+str(box1))
    print("Box2: "+str(box2))
    print(str(box1[0])+" * "+str(box2[0])+" = (part b): "+str(total))
        
if __name__ == "__main__":
    filename = "input/day8.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day8(filename)
