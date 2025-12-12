import math
import sys

from mainUtils import read_input_split
from z3 import Optimize, Int

def create_search_problem(prob_list):
    goal = prob_list[0]
    goal_list = []
    goal_size = len(goal) - 2

    joltage = prob_list[len(prob_list) - 1]
    joltage = joltage[1:-1]
    goal_list = list(map(int, joltage.split(",")))
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

def solve(goal_size, goal_list, moves):   
    solver = Optimize()
    if not solver:
        print("Could not create solver")
        return
    
    ## [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # J1 = 3, J2 = 5, J3 = 4, J4 = 7
    # J1 = 0(B1) + 0(B2) + 0(B3) + 0(B4) + 1(B5) + 1(B6) = B5 + B6 = 3
    # etc.
    vars = []
    for i in range(0, len(moves)):
        var = Int("B"+str(i))
        vars.append(var)
        solver.add(var >= 0)
    print("Solver var count: "+str(len(vars)))
    
    # Constraints from joltages
    for j in range(0, goal_size):
        m_vars = []
        for i in range(0, len(moves)):
            m = moves[i]
            if j in m:
                m_vars.append(vars[i])
        print("M_vars: "+str(m_vars))
        solver.add(sum(m_vars) == goal_list[j])
    
    solver.minimize(sum(vars))
    solver.check()
    result = solver.model()
    print(result)
    total = 0
    for r in result.decls():
        total += result[r].as_long()
    return total

def day10b(filename):
    print("aoc2025 day10b")
    problems = read_input_split(filename, " ")
    print(problems)

    total = 0
    for prob in problems:
        print(prob)
        goal_size, goal_list, moves = create_search_problem(prob)
        total += solve(goal_size, goal_list, moves)
        
    print("Fewest Button Presses (part b): "+str(total))
        
    
if __name__ == "__main__":
    filename = "input/day10.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        
    day10b(filename)