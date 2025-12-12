import math
import sys

from mainUtils import read_input_split
from search import Node, SearchProblem
              
# Would have been nice if this worked, but the search space is too large
# Maybe a better heuristic function?
# In any case, we'll use a linear algebra solver instead, day10b
class SearchProblem_10B(SearchProblem):
    # TODO: Could add a list of goal nodes
    def __init__(self, start, goal_joltage, moves):
        self.start_node = start
        self.start_node.g = 0
        self.goal_state = goal_joltage
        self.moves = moves
    
    # Can't go down in joltage, so if we go over the goal, we're done
    def is_invalid(self, node):
        for i in range(0, len(node.state)):
            if self.goal_state[i] < node.state[i]:
                return True
            
    def apply_move(self, node, move):
        next_state = node.state.copy()
        for m in move:
            next_state[m] = int(next_state[m] + 1)
        nxt = Node(len(node.state))
        nxt.state = next_state
        nxt.action = move
        return nxt            

def create_search_problem(prob_list):
    goal = prob_list[0]
    goal_list = []
    goal_size = len(goal) - 2

    for i in range(0, len(goal)):
        if goal[i] == '#':
            goal_list.append(i-1)
    print("Goal: "+str(goal_list))
    print("Goal state size: "+str(goal_size))
 
    moves = []
    for i in range(1, len(prob_list) - 1):
        nxt_move = eval(prob_list[i])
        if type(nxt_move) is tuple:
            nxt_move = list(nxt_move)
        elif type(nxt_move) is not list:
            nxt_move = [nxt_move]
            
        moves.append(nxt_move)
        
    print("Moves:")
    print(str(moves))
    return goal_size, goal_list, moves

def search(size, goal, moves):
    first_node = Node(size)
    print("Open Node: "+str(first_node.state))
    search = SearchProblem(first_node, goal, moves)
        
    best_path = search.a_star(first_node)
    if best_path is not None:
        return search.get_path(best_path)
    return None

def day10(filename):
    print("aoc2025 day10")
    problems = read_input_split(filename, " ")
    print(problems)
        
    total = 0
    for prob in problems:
        size, goal, moves = create_search_problem(prob)
        search_result = search(size, goal, moves)
        print("Search Result: "+str(search_result))
        if search_result is not None:
            print("Length: "+str(len(search_result)))
            total += len(search_result)
                
    print("Fewest Button Presses (part a): "+str(total))
    
    #total = 0
    #for prob in problems:
    #    size, goal, moves = create_search_problem(prob, B=True)
    #    search_result = search(size, goal, moves, B=True)
    #    print("Search Result: "+str(search_result))
    #    if search_result is not None:
    #        print("Length: "+str(len(search_result)))
    #        total += len(search_result)
    #    
    #print("Fewest Button Presses (part b): "+str(total))
         
if __name__ == "__main__":
    filename = "input/day10.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day10(filename)