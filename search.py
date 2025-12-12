# Search utilities
# TODO: Generalize this
#  For now, the node is specific for the Day10 problem
import math
import heapq

# Search node where the state is an array of booleans 
class Node:
    def __init__(self, size):
        self.state = [0] * size
        self.action = None # Action to get to this node
        self.parent = None # Previons node, we took Action to get from there to here
        # A* metrics
        self.f = float('inf')
        self.g = float('inf')
        self.h = 0
    
    def state_str(self):
        val = ""
        for i in self.state:
            val += str(i)
            val += ","
        return val
    
    def __lt__(self, other):
        return self.h <= other.h
    
    def __gt__(self, other):
        return self.h >= other.h
                

class SearchProblem:
    # TODO: Could add a list of goal nodes
    def __init__(self, start, goal, moves):
        self.start_node = start
        self.start_node.g = 0
        self.goal_state = [0] * len(start.state)
        for i in range(0, len(start.state)):
            if i in goal:
                self.goal_state[i] = 1
            else:
                self.goal_state[i] = 0
        self.moves = moves
           
    def apply_move(self, node, move):
        next_state = node.state.copy()
        for m in move:
            next_state[m] = int(not next_state[m])
        nxt = Node(len(node.state))
        nxt.state = next_state
        nxt.action = move
        return nxt
    
    def is_goal(self, node):
        return node.state == self.goal_state
    
    # Subclasses can override
    def is_invalid(self, node):
        return False
    
    def calculate_h(self, node):
        count = 0
        for i in range(0, len(node.state)):
            count += abs(node.state[i] - self.goal_state[i])
        return count
    
    def print_path(self, node):
        print(node.action)
        cur = node
        while cur.parent is not None:
            cur = cur.parent
            if cur.action is not None:
                print(" <- " + str(cur.action))
            
    def get_path(self, node):
        path = []
        path.append(node.action)
        cur = node
        while cur.parent is not None:
            cur = cur.parent
            if cur.action is not None:
                path.insert(0, cur.action)
        return path

    def a_star(self, node):
        if self.is_goal(node):
            print("Already at the goal node")
            return
        
        closed_set = {}
        open_list = []
        open_set = {}
        heapq.heappush(open_list, node)
        best_goal = None
        
        while len(open_list) > 0:
            next = heapq.heappop(open_list)
            # print("Searching node: "+next.state_str()+"  OpenList: "+str(len(open_list)))
            for move in self.moves:
                nbr = self.apply_move(next, move)
                if self.is_invalid(nbr):
                    continue
                nbr.parent = next
                nbr.g = next.g + 1
                            
                if best_goal is not None and best_goal.g <= nbr.g:
                    continue
                
                nbr_state = nbr.state_str()
                if nbr_state in closed_set:
                    existing_node = closed_set[nbr_state]
                    if existing_node.g <= nbr.g:
                    # We have a better path to this state, prune this
                        continue
                if self.is_goal(nbr):
                    print("Found a goal node: "+nbr_state+": "+str(nbr.g))
                    print("  From move: "+str(move)+" to node: "+next.state_str()+" -> "+nbr.state_str())
                    if best_goal is None or best_goal.g > nbr.g:
                        print("Found a better goal node g: "+str(nbr.g))
                        best_goal = nbr
                        continue
                    
                nbr.h = self.calculate_h(nbr)
                nbr.f = nbr.g + nbr.h
                
                cur_open = None
                if nbr_state in open_set:
                    cur_open = open_set[nbr_state]
                if cur_open is None or cur_open.f > nbr.f:
                    # Found a better node, drop the old one from the openset
                    # print("Adding move: "+str(move)+" to node: "+next.state_str()+" -> "+nbr.state_str())
                    if cur_open in open_list:
                        open_list.remove(cur_open)
                    open_set[nbr_state] = nbr
                    heapq.heappush(open_list, nbr)
                    
            closed_set[next.state_str()] = next
        
        if best_goal is None:
            print("Unable to find any path to the goal!")
            return
                    
        print("Best goal: "+str(best_goal.g))
        self.print_path(best_goal)
        return best_goal
            
                
                   
                    
        
        
        