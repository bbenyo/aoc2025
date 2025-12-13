import math
import sys

from mainUtils import read_input_split_whitespace

class Node:
    def __init__(self, name):
        self.label = name
        self.edges = []
    
    def add_edge(self, name):
        self.edges.append(name)
        
    def __str__(self):
        val = self.label + " -> "
        for i in self.edges:
            val += str(i)
            val += ", "
        return val
    
class SearchNode:
    def __init__(self, name):
        self.label = name
        self.path = []
    
    def __str__(self):
        val = self.label + " <- "
        for i in self.path:
            val += str(i)
            val += " <- "
        return val
        
    # Follow an edge, create a new node
    def move(self, edge):
        new_node = SearchNode(edge)
        if len(self.path) > 0:
            new_node.path.extend(self.path)
        new_node.path.append(self.label)
        return new_node
    
    
def count_dfs(nodes, s_node, goal_label, cache, require=[]):
    path_count = 0
    node = nodes[s_node.label]
    
    cache_key = s_node.label
    for req in require:
        if req in s_node.path or req == s_node.label:
            cache_key += req
    
    if cache_key in cache:
        return cache[cache_key]
    
    for edge in node.edges:
        new_node = s_node.move(edge)
        if new_node.label == goal_label:
            found_all = True
            if require is not None:
                for req in require:
                    if req not in new_node.path:
                        found_all = False
                        break
            if found_all:
                print("Found path: "+str(new_node.path))
                path_count += 1
        elif new_node.label != "out":
            if new_node.label in new_node.path:
                print("Would be a cycle: "+new_node)
            else:
                path_count += count_dfs(nodes, new_node, goal_label, cache, require)
                
    print("Cache: "+cache_key+" = "+str(path_count))
    cache[cache_key] = path_count
    return path_count
                
def day11(filename):
    print("aoc2025 day11")
    devices = read_input_split_whitespace(filename)
    
    nodes = {}
    for device in devices:
        label = device[0][:-1]
        node = Node(label)
        for i in range(1, len(device)):
            node.add_edge(device[i])
        print(node)
        nodes[label] = node
    
    cache = {}
    if "you" in nodes:
        count = count_dfs(nodes, SearchNode("you"), "out", cache)
    
        print("Path count (part a): "+str(count))
    
    cache = {}
    count = count_dfs(nodes, SearchNode("svr"), "out", cache, require=["fft", "dac"])
    print("Path count (part b): "+str(count))
        
if __name__ == "__main__":
    filename = "input/day11.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day11(filename)
